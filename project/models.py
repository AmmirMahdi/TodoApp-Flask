from project import db  
from datetime import datetime


"""

    Each user can have many todos 

    user -> todo ONE TO ONE 


"""

class User(db.Model):
    
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    location = db.Column(db.String(64))
    todos    = db.relationship('Todo', backref='user')

    def __repr__(self):
        return self.username 
    def __str__(self):
        return self.username 



class Todo(db.Model):
    __tablename__='todos'
    
    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.Text, nullable=False)
    date         = db.Column(db.Date, default=datetime.utcnow())
    description  = db.Column(db.String(128))
    complete     = db.Column(db.Boolean)
    users        = db.Column('User', db.ForeignKey('users.id'))

    def __str__(self):
        return self.users 
    

    def __repr__(self):
        return f"Todo {self.title}"

