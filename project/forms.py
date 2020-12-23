from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    complete = BooleanField('complete')