from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class SongsDeleter(FlaskForm):
    ID = StringField("ID: ", [validators.regexp('^[2-500]$', flags=0, message='Input number greater the 0')])
    name = StringField("Name: ")

    band = StringField("Band: ")

    submit = SubmitField("Send")
