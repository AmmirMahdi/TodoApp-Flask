from project import app, db
from flask import render_template, url_for, redirect
from project.forms import TodoForm
from project.models import Todo

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


@pp.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    print('Todo Deleted !')