from flask import Flask
from flask_cors import CORS, cross_origin
import os

from src.database.bookmark import Bookmark
from src.database.user import User

from src.database import db

from flask_jwt_extended import JWTManager


'''
# This is the example of getting variable from normal .env
from decouple import config
config['JWT_SECRET_KEY']
'''


test_config = None

app = Flask(__name__, instance_relative_config=True)
CORS(app)

if test_config is None:
    app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    )
else:
    app.config.from_mapping(test_config)



'''
db.app = app
db.init_app(app)
app.app_context().push()
db.create_all()
'''
db.init_app(app)
app.app_context().push()
# db.create_all() # Uncommented this line only to create database with new tables during the running the application




JWTManager(app)
