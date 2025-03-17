from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = EmailField(
        label="Email",
        validators=[
            DataRequired(),
            Email(message="That's not a valid email address."),
            Length(min=6, message='Little short for an email address?')
        ]
    )
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = "cBb#CPhVf6sz)A,}=8s8md2uiWn.,A=#%G)j#2p7V3D1n24-c_pAXM]%zQcstH+NduCZ7ryoGw+=o*D7e>J=H]y*bL=1BN0w},_Z"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()

    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect(url_for("true"))

        return redirect(url_for("false"))

    return render_template(template_name_or_list='login.html', form=form)


@app.route("/denied")
def false():
    return render_template("denied.html")


@app.route("/success")
def true():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)
