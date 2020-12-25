from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField,TextAreaField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title  = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    complete = BooleanField('Complete')
    submit = SubmitField('Submit')

class DelTodo(FlaskForm):
    id = IntegerField('id')
    submit = SubmitField('submit')