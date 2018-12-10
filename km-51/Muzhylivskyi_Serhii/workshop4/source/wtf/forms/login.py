from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class LoginForm(FlaskForm):
    login = StringField("Login: ", [validators.DataRequired("Required")])
    password = PasswordField("Password: ", [validators.DataRequired("Required")])

    submit = SubmitField("Sign In")
