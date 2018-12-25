from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class BandReader(FlaskForm):
    name = StringField("Name: ", [validators.DataRequired("Required")])

    submit = SubmitField("Submit")
