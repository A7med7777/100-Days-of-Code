import requests

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


def get_post():
    url = "https://api.npoint.io/244f2ff49becd888754b"

    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as re:
        return [{"title": re}]


response = get_post()


@app.route("/")
def hello():
    global response
    response = get_post()
    return render_template("index.html", data=response)


@app.route("/post/<int:post_id>")
def post(post_id):
    global response

    for data in response:
        if data["id"] == post_id:
            post_data = data
            return render_template("post.html", post=post_data)

    return redirect(url_for('hello'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
