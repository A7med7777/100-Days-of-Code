import smtplib
import os

from flask import Flask, render_template, request
import requests

EMAIL = os.getenv("MY_EMAIL")
PASS = os.getenv("MY_PASS")

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template(template_name_or_list="index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    msg = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASS)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,
                    msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n\t{message}\n"
                )

            msg = "Email sent!"
        except Exception:
            msg = "Error sending email"

    return render_template(template_name_or_list="contact.html", msg=msg)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template(template_name_or_list="post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
