from project import app
from flask import render_template, url_for, redirect
from project.forms import TodoForm
from project.models import Todo

@app.route('/')
def index():

    form = TodoForm()

    if form.validate_on_submit():
        new_todo = Todo(title=form.title.data, complete=form.complete.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect('todo.html')
    return render_template('index.html', form=form)
    


    return render_template('index.html')