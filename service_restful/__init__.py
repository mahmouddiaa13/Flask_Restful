from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_migrate import Migrate
from flask_restful import Api
from service_restful.config import URI

app = Flask(__name__)
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['MONGO_DBNAME'] = 'mongodatab'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mongodatab'
# db = SQLAlchemy(app)
db = PyMongo(app)
migrate = Migrate(app, db)

from service_restful.routes.users import HandleUsers
