from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class SongsInPlayListController(FlaskForm):
    name = StringField("ID: ")

    submit = SubmitField("Send")
