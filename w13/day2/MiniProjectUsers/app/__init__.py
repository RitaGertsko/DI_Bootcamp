import flask_migrate
import flask_sqlalchemy
from flask import Flask
from app.config import Config
import json

my_app = Flask(__name__)

my_app.config.from_object(Config)

db = flask_sqlalchemy.SQLAlchemy(my_app)
migrate = flask_migrate.Migrate(my_app, db)

from app.models import User

def populate():
    with open('users.json', 'r') as f:
        database = json.load(f)
    for data in database:
        new_user = User(
            user_id=data['id'],
            userName=data['name'],
            userStreet=data['address']['street'],
            userCity=data['address']['city'],
            zipCode=data['address']['zipcode'])
        db.session.add(new_user)
    db.session.commit()
    return


# populate()

from app import routes
