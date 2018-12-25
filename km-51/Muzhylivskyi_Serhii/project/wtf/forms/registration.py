from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class RegForm(FlaskForm):
    login = StringField("Login: ", [validators.DataRequired("Required")])
    password = PasswordField("Password: ", [validators.DataRequired("Required")])
    name = StringField("Name: ", [validators.data_required("Required")])
    email = StringField("Email: ", [validators.data_required("Required"), validators.email])

    submit = SubmitField("Sign Up")
