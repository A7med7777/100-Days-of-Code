# import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, request, jsonify
from flask_cors import CORS


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(123), unique=True)
    author: Mapped[str] = mapped_column(String(123), nullable=False)
    read: Mapped[bool] = mapped_column(Boolean)


with app.app_context():
    db.create_all()

# BOOKS = [
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ]

app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


@app.route("/books", methods=["GET", "POST"])
def all_books():
    response_object = {'status': 'success'}

    if request.method == "POST":
        post_data = request.get_json()

        if not post_data["title"] or not post_data["author"]:
            return jsonify({"error": "Invalid payload. 'title', and 'author' fields are required."}), 400

        book = Book(title=post_data.get("title"), author=post_data.get("author"), read=post_data.get("read"))
        db.session.add(book)
        db.session.commit()
        response_object['message'] = 'Book added!'
    else:
        books_list = []
        books = db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()

        for book in books:
            books_list.append({'id': book.id, 'title': book.title, 'author': book.author, 'read': book.read})

        response_object['books'] = books_list

    return jsonify(response_object)


@app.route("/books/<book_id>", methods=["PUT", "DELETE"])
def single_book(book_id):
    found = False
    book = db.get_or_404(Book, book_id)
    response_object = {'status': 'success'}

    if request.method == "PUT":
        post_data = request.get_json()
        book.title = post_data.get("title")
        book.author = post_data.get("author")
        book.read = post_data.get("read")

        try:
            db.session.commit()
            found = True
            response_object['message'] = 'Book updated!'
        except Exception:
            db.session.rollback()
            found = False

    if request.method == "DELETE":
        db.session.delete(book)

        try:
            db.session.commit()
            found = True
            response_object['message'] = 'Book removed!'
        except Exception:
            db.session.rollback()
            found = False

    if not found:
        return jsonify({"error": "This book id does not exist."}), 400

    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)
