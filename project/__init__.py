import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config app 
basedir = os.path.abspath(os.path.dirname(__file__))
#  secret key 
app.config['SECRET_KEY'] = 'My Secret Key' 

#  DATABASE  Configuration
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMT_TRECK_MODIFICATION'] = False 

db = SQLAlchemy(app)



from project import routes
from project import models
from project import forms
