from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class AddForm(FlaskForm):
    name = StringField(label="City`s Name: ",
                       validators=[DataRequired(message="Please Enter City's Name"), Length(min=1, max=15)])
    country = StringField(label="City`s Country: ",
                          validators=[DataRequired(message="Please Enter City's Country")])
    residents = IntegerField(label="City`s Residents Number: ",
                             validators=[DataRequired()])
    area = IntegerField(label="City`s area in square km: ", validators=[Optional()])
    latitude = IntegerField(label="City`s Latitude: ", validators=[Optional()])
    longitude = IntegerField(label="City`s Longitude: ", validators=[Optional()])
    submit = SubmitField("Submit")
