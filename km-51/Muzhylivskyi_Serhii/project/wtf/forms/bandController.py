from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class BandController(FlaskForm):
    name = StringField("Name: ", [validators.DataRequired("Required")])

    music_label = StringField("Music Label: ", [validators.DataRequired("Required")])

    submit = SubmitField("Send")
