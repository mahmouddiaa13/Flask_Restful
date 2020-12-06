from service_restful.crud import Crud
from flask import request
from service_restful.models.users.users import Users
from service_restful import db


class UserCrud(Crud):

    def post(self):
        if request.is_json:
            data = request.get_json()
            new_user = Users(username=data['username'], email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"User {new_user.username} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    def get(self):
        users = Users.query.all()
        results = [
            {
                "username": user.username,
                "email": user.email
            } for user in users]

        return {"count": len(results), "Users": results}

    def getById(self, user_id):
        user = Users.query.get_or_404(user_id)
        response = {
            "username": user.username,
            "email": user.email
        }
        return {"message": "success", "user": response}

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
