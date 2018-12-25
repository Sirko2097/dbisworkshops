from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class UpdateUser(FlaskForm):
    password = PasswordField("Password: ")
    name = StringField("Name: ")
    email = StringField("Email: ", [validators.email])

    submit = SubmitField("Confirm changes")
