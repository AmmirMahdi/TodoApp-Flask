from project import app, db
from flask import render_template, url_for, redirect
from project.forms import TodoForm, DelTodo
from project.models import Todo

from datetime import datetime

from sqlalchemy import asc

# Add 
@app.route('/', methods=['GET', 'POST'])
def index():

    form = TodoForm()

    if form.validate_on_submit():
        new_todo = Todo(title=form.title.data, complete=form.complete.data)
        db.session.add(new_todo)
        db.session.commit()
        print("todo added")
        return redirect('todo')
    return render_template('index.html', form=form, current_time=datetime.utcnow())
    
#  Todo List  
@app.route('/todo')
def todo():
    todo = Todo.query.all()
    return render_template('todo.html', todo=todo)


#  Update
@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete 
    print('todo update')
    db.session.commit()
    return redirect(url_for('todo'))

#  Delete Todo
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    print("we are in delete function ")
    print(todo)
    db.session.delete(todo)
    db.session.commit()
    print('Deleted !')
    return redirect(url_for('index'))
