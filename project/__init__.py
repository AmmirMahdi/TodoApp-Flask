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


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mywebdev23@gmail.com'    
app.config['MAIL_PASSWORD'] = 'amirmahdirashvand5329@@@@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

from flask_mail import Mail 
mail = Mail()


mail.init_app(app)

###############################################3
from project import routes
from project import models
from project import forms
from project import custom_error
