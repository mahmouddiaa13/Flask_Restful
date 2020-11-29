from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:M@7m0ud@localhost:5432/cars_owner"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<User {self.username}>"


class HandleUsers(Resource):
    def get(self):
        users = Users.query.all()
        results = [
            {
                "username": user.username,
                "email": user.email
            } for user in users]

        return {"count": len(results), "Users": results}

    def post(self):
        if request.is_json:
            data = request.get_json()
            new_user = Users(username=data['username'], email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"User {new_user.username} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}


class HandleUser(Resource):
    def get(self, user_id):
        user = Users.query.get_or_404(user_id)
        response = {
            "username": user.username,
            "email": user.email
        }
        return {"message": "success", "car": response}

    def put(self, user_id):
        user = Users.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data['username']
        user.email = data['email']
        db.session.add(user)
        db.session.commit()
        return {"message": f"User {user.username} successfully updated"}

    def delete(self, user_id):
        user = Users.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.username} successfully deleted."}


api.add_resource(HandleUsers, '/HandleUsers')
api.add_resource(HandleUser, '/HandleUsers/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
