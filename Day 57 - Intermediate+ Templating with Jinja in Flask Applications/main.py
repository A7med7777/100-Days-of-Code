import datetime as dt
import requests

from flask import Flask, render_template
from markupsafe import escape
from random import randint

app = Flask(__name__)


@app.route("/")
def hello():
    random_num = randint(0, 9)
    year = dt.datetime.now().year
    company = "Ahmed Hussein"
    copyrights = f"© {year}, {company}."
    return render_template(template_name_or_list="index.html", num=random_num, copyright=copyrights)


@app.route("/guess/<name>")
def guess(name):
    the_name = escape(name)
    url = f"https://api.genderize.io/?name={the_name}"
    genderize_response = requests.get(url).json()["gender"]
    url = f"https://api.agify.io/?name={the_name}"
    agify_response = requests.get(url).json()["age"]
    url = f"https://api.nationalize.io/?name={the_name}"
    nationalize_response = requests.get(url).json()["country"][0]["country_id"]

    return render_template(
        template_name_or_list="guess.html",
        name=the_name.title(),
        gender=genderize_response,
        age=agify_response,
        nation=nationalize_response
    )


@app.route("/blog")
def blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_posts = requests.get(url).json()
    return render_template(template_name_or_list="blog.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
