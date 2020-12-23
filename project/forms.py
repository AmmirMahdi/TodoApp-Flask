from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField()
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title  = StringField('title', validators=[DataRequired()])
    complete = BooleanField('complete')
    submit = SubmitField('submit')

class DelTodo(FlaskForm):
    id = IntegerField('id')
    submit = SubmitField('submit')