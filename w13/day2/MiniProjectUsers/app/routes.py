from app import my_app
from flask import render_template
from app.models import User


@my_app.route('/', methods=['GET', 'POST'])
def home():
    all_the_users = User.query.all()
    return render_template("index.html", data=all_the_users)
