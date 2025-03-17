import os

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.expression import func
from sqlalchemy import Integer, String, Boolean
from werkzeug.exceptions import NotFound

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Café TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalars().first()

    if not cafe:
        return jsonify(error={"Not Found": "No cafes found in the database."}), 404

    return jsonify(cafe=cafe.to_dict())


@app.route("/cafes")
def all_cafes():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    location = request.args.get("loc")

    if not location:
        return jsonify(error={"Bad Request": "Location parameter is required."}), 400

    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()

    if not cafes:
        return jsonify(error={"Not Found": "No cafes found at the specified location."}), 404

    return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200


@app.route("/add", methods=["POST"])
def post_new_cafe():
    try:
        data = request.get_json()

        new_cafe = Cafe(
            name=data.get("name"),
            map_url=data.get("map_url"),
            img_url=data.get("img_url"),
            location=data.get("location"),
            has_sockets=data.get("has_sockets", False),
            has_toilet=data.get("has_toilet", False),
            has_wifi=data.get("has_wifi", False),
            can_take_calls=data.get("can_take_calls", False),
            seats=data.get("seats"),
            coffee_price=data.get("coffee_price"),
        )

        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error={"Internal Server Error": "Failed to add the cafe.", "details": str(e)}), 500


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    try:
        new_price = request.args.get("new_price")

        if not new_price:
            return jsonify(error={"Bad Request": "New price parameter is required."}), 400

        cafe = db.get_or_404(Cafe, cafe_id)
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    except NotFound:
        return jsonify(error={"Not Found": "Cafe not found with the given ID."}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify(error={"Internal Server Error": "Failed to update the price.", "details": str(e)}), 500


@app.route("/cafe/<int:cafe_id>/delete", methods=["DELETE"])
def user_delete(cafe_id):
    api_key = request.headers.get("Authorization")

    if api_key == os.getenv("API_KEY"):
        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        except NotFound:
            return jsonify(error={"Not Found": "Cafe not found with the given ID."}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify(error={"Internal Server Error": "Failed to delete the cafe.", "details": str(e)}), 500
    else:
        return jsonify(error={"Forbidden": "Invalid API key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
