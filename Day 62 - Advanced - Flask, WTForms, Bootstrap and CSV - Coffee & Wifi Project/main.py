from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TimeField, URLField
from wtforms.validators import DataRequired, URL

import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = URLField(label='Cafe location on google maps(URL)', validators=[DataRequired(), URL()])
    open = TimeField(label='Opining time', validators=[DataRequired()])
    close = TimeField(label='Closing time', validators=[DataRequired()])

    coffee = SelectField(
        label='Coffee rating',

        choices=[
            ("✘", "✘"),
            ("☕", "☕"),
            ("☕☕", "☕☕"),
            ("☕☕☕", "☕☕☕"),
            ("☕☕☕☕", "☕☕☕☕"),
            ("☕☕☕☕☕", "☕☕☕☕☕")
        ]
    )

    wifi = SelectField(
        label='Wifi strength rating',

        choices=[
            ("✘", "✘"),
            ("💪", "💪"),
            ("💪💪", "💪💪"),
            ("💪💪💪", "💪💪💪"),
            ("💪💪💪💪", "💪💪💪💪"),
            ("💪💪💪💪💪", "💪💪💪💪💪")
        ]
    )

    power = SelectField(
        label='Power socket rating',

        choices=[
            ("✘", "✘"),
            ("🔌", "🔌"),
            ("🔌🔌", "🔌🔌"),
            ("🔌🔌🔌", "🔌🔌🔌"),
            ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
            ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")
        ]
    )

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        with open("./cafe-data.csv", "a", encoding="utf-8") as file:
            for key, value in form.data.items():
                if key not in ["submit", "csrf_token"]:
                    if key in ["open", "close"]:
                        time_12hr = value.strftime("%I:%M %p")  # Get the 12-hour time
                        file.write(f"{time_12hr}" + ", ")
                    else:
                        file.write(f"{value}" + (", " if key != "power" else "\n"))

        return redirect(url_for("add_cafe"))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []

        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
