from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired
import requests


class EditForm(FlaskForm):
    rating = FloatField(
        "your rating out of 10 e.g. 7.5".title(),
        validators=[DataRequired(message="Please provide a rating between 0 and 10.")]
    )
    review = StringField("your review".title(), validators=[DataRequired()])
    submit = SubmitField("done".title())


class AddForm(FlaskForm):
    title = StringField("movie title".title(), validators=[DataRequired()])
    submit = SubmitField("add movie".title())


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# initialize the app with the extension
db.init_app(app)
Bootstrap5(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    for index, movie in enumerate(movies):
        movie.ranking = len(movies) - index

    db.session.commit()
    return render_template(template_name_or_list="index.html", movies=movies)


@app.route("/movies/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()

    if add_form.validate_on_submit():
        url = "https://api.themoviedb.org/3/search/movie"
        params = {"query": add_form.title.data, "page": 1}

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyOGY5OWNkYjgwZTQ4M2M3NmNiOTRhMDExODQ0ZjQ1OCIsIm5iZ"
                             "iI6MTcxNzE3MDg3OS44MjksInN1YiI6IjY2NTlmMmJmNWFlZmIwZmM2ZjcxNjBmZiIsInNjb3BlcyI6WyJhcGlfcm"
                             "VhZCJdLCJ2ZXJzaW9uIjoxfQ.J0lPpuateu_dpPBpEA4BhwwcmbzHosorxRqetOtVjFo"
        }

        response = requests.get(url, headers=headers, params=params)

        return render_template("select.html", movies=response.json())

    return render_template("add.html", add_form=add_form)


@app.route("/movies/create", methods=["GET", "POST"])
def movie_create():
    url = f"https://api.themoviedb.org/3/movie/{request.args.get("id")}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyOGY5OWNkYjgwZTQ4M2M3NmNiOTRhMDExODQ0ZjQ1OCIsIm5iZiI6M"
                         "TcxNzE3MDg3OS44MjksInN1YiI6IjY2NTlmMmJmNWFlZmIwZmM2ZjcxNjBmZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLC"
                         "J2ZXJzaW9uIjoxfQ.J0lPpuateu_dpPBpEA4BhwwcmbzHosorxRqetOtVjFo"
    }

    response = requests.get(url, headers=headers).json()

    new_movie = Movie(
        title=response["original_title"],
        year=response["release_date"].split("-")[0],
        description=response["overview"],
        review=response["tagline"],
        img_url=f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
    )

    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/movie/<int:id>", methods=["GET", "POST"])
def movie_detail(id):
    movie = db.get_or_404(Movie, id, description=f"No movie with the id '{id}'.")
    edit_form = EditForm(rating=movie.rating, review=movie.review)

    if edit_form.validate_on_submit():
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", edit_form=edit_form)


@app.route("/movie/<int:id>/delete")
def movie_delete(id):
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
