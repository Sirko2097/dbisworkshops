from flask_wtf import FlaskForm
from wtforms import StringField, validators


class BandForm(FlaskForm):
    name = StringField("Input Name: ", [validators.DataRequired("Required")])

    music_label = StringField("Input Music Label: ", [validators.DataRequired("Required")])
