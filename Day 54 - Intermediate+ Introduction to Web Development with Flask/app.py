from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return ('<h1>Hello, World</h1>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGpncno1MzI0bXV2bWNkd3l1bnNzYmI1dG0wMWowanEyM2Vhc29'
            'ydiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0PCaiggZ7ffqOb8Esw/giphy.gif">')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:sub_path>')
def show_sub_path(sub_path):
    # show the sub_path after /path/
    return f'Sub path {escape(sub_path)}'


if __name__ == "__main__":
    app.run(debug=True)
