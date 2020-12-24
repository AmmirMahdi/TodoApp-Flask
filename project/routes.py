from project import app, db
from flask import render_template, url_for, redirect
from project.forms import TodoForm, DelTodo
from project.models import Todo

from sqlalchemy import asc

@app.route('/', methods=['GET', 'POST'])
def index():

    form = TodoForm()

    if form.validate_on_submit():
        new_todo = Todo(title=form.title.data, complete=form.complete.data)
        db.session.add(new_todo)
        db.session.commit()
        print("todo added")
        return redirect('todo')
    return render_template('index.html', form=form)
    
@app.route('/todo')
def todo():
    todo = Todo.query.all()
    return render_template('todo.html', todo=todo)


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    print("we are in delete function ")
    print(todo)
    db.session.delete(todo)
    db.session.commit()
    print('Deleted !')
    return redirect(url_for('index'))
