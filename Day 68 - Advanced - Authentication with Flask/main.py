from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = "./static/files/"


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password = request.form.get("password")
        password_hash = generate_password_hash(password, method='pbkdf2', salt_length=16)

        try:
            new_user = User(
                email=request.form.get("email"),
                password=password_hash,
                name=request.form.get("name")
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))
        except IntegrityError:
            flash("You've already signed up with that email, log in instead!", category="error")

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You're already logged in.", category="error")
        return redirect(url_for("home"))
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for("secrets"))
            else:
                flash("Password incorrect, please try again.", category="error")
        else:
            flash("That email does not exist, please try again.", category="error")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/uploads/<path:name>")
@login_required
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
