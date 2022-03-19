from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Optional


class Form(FlaskForm):
    firstName = StringField(label="First Name: ",
                            validators=[DataRequired(message="Please Enter Your First Name"), Length(min=2, max=25)])
    lastName = StringField(label="Last Name: ",
                           validators=[DataRequired(message="Please Enter Your Last Name"), Length(min=2, max=25)])
    email = EmailField(label="Email: ", validators=[DataRequired(message="Please Enter Your Email")])
    address = StringField(label="Address: ", validators=[DataRequired()])
    phoneNumber = IntegerField('Phone Number', validators=[DataRequired()])

    instituteName = StringField(label='Institute: ', validators=[DataRequired()])
    educationType = StringField(label='Education: ', validators=[DataRequired()])
    started = DateField(label='From: ', format='%d-%m-%Y', validators=[Optional()])
    ended = DateField(label='Until: ', format='%d-%m-%Y', validators=[Optional()])

    instituteName2 = StringField(label='Institute: ', validators=[Optional()])
    educationType2 = StringField(label='Education Type: ', validators=[Optional()])
    started2 = DateField(label='From: ', format='%d-%m-%Y', validators=[Optional()])
    ended2 = DateField(label='Until: ', format='%d-%m-%Y', validators=[Optional()])

    companyName = StringField(label='Company Name: ', validators=[Optional(), Length(min=2, max=15)])
    position = StringField(label='Position: ', validators=[Optional(), Length(min=2, max=25)])
    startedWork = DateField(label='From: ', format='%d-%m-%Y', validators=[Optional()])
    endedWork = DateField(label='Until: ', format='%d-%m-%Y', validators=[Optional()])

    skill1 = StringField(label='Skill 1: ', validators=[Optional(), Length(min=2, max=25)])
    skill2 = StringField(label='Skill 2 (Optional): ', validators=[Optional(), Length(min=2, max=25)])

    hobbieInfo = TextAreaField(label='Tell about this hobbies (Optional): ',
                               validators=[Optional(), Length(min=2, max=200)])

    submit = SubmitField("Submit")
