from project import db  

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.Text, nullable=False)
    complete = db.Column(db.Boolean)
