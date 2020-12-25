from project import db  
from datetime import datetime
class Todo(db.Model):
    __tablename__='todo'
    
    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.Text, nullable=False)
    date         = db.Column(db.Date, default=datetime.utcnow())
    description  = db.Column(db.Text)
    complete     = db.Column(db.Boolean)
