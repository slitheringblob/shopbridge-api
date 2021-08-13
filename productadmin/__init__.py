from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

##initialize the app
app = Flask(__name__)


##setting the current path as basedir to be used as a relative path for all other files
apibase = os.path.abspath(os.path.dirname(__file__))
##base config for the API
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(apibase,'inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
##initialize sqlalchemy and marhsmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
#import routes after app is created and db object is initialized
from productadmin import routes