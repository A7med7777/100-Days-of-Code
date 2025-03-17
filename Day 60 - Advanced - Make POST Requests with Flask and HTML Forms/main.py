from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form.get("name")
    password = request.form.get("password")
    return f"<h1>{name}</h1><h2>{password}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
