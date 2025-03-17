import requests

from flask import Flask, render_template
from post import Post

app = Flask(__name__)


def get_json():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    posts = []

    for post in response.json():
        new_post = Post(post)
        posts.append(new_post)

    return posts


posts = get_json()


@app.route('/')
def home():
    all_posts = get_json()
    return render_template(template_name_or_list="index.html", posts=all_posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    required_post = None

    for post in posts:
        if post.id == post_id:
            required_post = post
            break

    return render_template(template_name_or_list="post.html", post=required_post)


if __name__ == "__main__":
    app.run(debug=True)
