from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField,TextAreaField,DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime

class TodoForm(FlaskForm):
    title  = StringField('Title', validators=[DataRequired()])
    # date   = DateTimeField('Date', default=datetime.utcnow())
    description = TextAreaField('Description')
    complete = BooleanField('Complete')
    submit = SubmitField('Submit')

class DelTodo(FlaskForm):
    id = IntegerField('id')
    submit = SubmitField('submit')