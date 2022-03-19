from app import cv_app
from flask import render_template, redirect, url_for, request
from app.forms import Form
import json

path = 'C:/Users/rita1/OneDrive/FullStack/week12/day2/DailyChallenge/database.json'

def open_database_file(data):
    with open(path, "w+") as f:
        json.dump(data, f, indent=4)


@cv_app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html", title='Home')


@cv_app.route('/form', methods=["GET", "POST"])
def my_form():
    form = Form()
    if form.validate_on_submit():
        results = request.form
        open_database_file(results)
        return redirect(url_for('cv'))

    return render_template("my_form.html", title='Personal Info', form=form)


@cv_app.route('/cv', methods=["GET", "POST"])
def cv():
    with open('database.json', 'r') as f:
        form_info = json.load(f)
    return render_template("cv.html", title='CV', data=form_info)
