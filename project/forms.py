from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title  = StringField('title', validators=[DataRequired()])
    complete = BooleanField('complete')
    submit = SubmitField('submit')
