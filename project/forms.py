from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title  = StringField('Title', validators=[DataRequired()])
    complete = BooleanField('Complete')
    submit = SubmitField('Submit')

class DelTodo(FlaskForm):
    id = IntegerField('id')
    submit = SubmitField('submit')