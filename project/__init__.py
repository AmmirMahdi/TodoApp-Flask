import os

##########################################
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#########################################

#  Boostrap 
from flask_bootstrap import Bootstrap

# Flask Momemnt extension for date and time 
from flask_moment import Moment 

app = Flask(__name__)



# config directory database app 
basedir = os.path.abspath(os.path.dirname(__file__))


#  secret key 
app.config['SECRET_KEY'] = 'My Secret Key' 

#  DATABASE  Configuration
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMT_TRECK_MODIFICATION'] = False 

db = SQLAlchemy(app)

#  Migration Database for change column and .. 
Migrate(app, db)


#  Boostrap module
bootstrap = Bootstrap(app)

# Moment For date time 
moment = Moment(app)
moment.init_app(app)


##############################################
#                                           #
#           Email Configuration             #
#                                           #
#                                           #
############################################


###############################################3
from project import routes
from project import models
from project import forms
from project import custom_error
