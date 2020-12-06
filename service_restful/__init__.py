from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from service_restful.config import URI

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from service_restful.routes.users import HandleUsersById, HandleUsers
