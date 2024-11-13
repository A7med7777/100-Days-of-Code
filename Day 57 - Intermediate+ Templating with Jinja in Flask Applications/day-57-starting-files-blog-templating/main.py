import requests

from flask import Flask, render_template
from post import Post

app = Flask(__name__)

posts = []


@app.route('/')
def home():
    global posts
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)

    for post in response.json():
        new_post = Post(post)
        posts.append(new_post)

    return render_template(template_name_or_list="index.html", posts=posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    required_post = None

    for post in posts:
        if post.id == post_id:
            required_post = post
            
    return render_template(template_name_or_list="post.html", post=required_post)


if __name__ == "__main__":
    app.run(debug=True)
