from project import db  
from datetime import datetime



class Todo(db.Model):
    __tablename__='todo'
    
    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.Text, nullable=False)
    date         = db.Column(db.Date, default=datetime.utcnow())
    description  = db.Column(db.Text)
    complete     = db.Column(db.Boolean)
    users        = db.relationship('User', backref='todo')

    def __repr__(self):
        return f"Todo {self.title}"


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    todo     = db.Column(db.Integer, db.ForeignKey('todo.id'))
    
    def __repr__(self):
        return f"User {self.username}"