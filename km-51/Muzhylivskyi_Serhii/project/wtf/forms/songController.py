from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class SongsController(FlaskForm):
    name = StringField("Name: ", [validators.DataRequired("Required")])
    duration = StringField("Duration: ", [validators.DataRequired("Required"),
                                          validators.regexp('^\\s*(?=.*[1-9])\\d*(?:\\.\\d{1,5})?\\s*$$', flags=0,
                                                            message='Enter positive double number.')])
    band = StringField("Band: ", [validators.DataRequired("Required")])
    genre = StringField("Genre: ", [validators.DataRequired("Required")])

    submit = SubmitField("Send")
