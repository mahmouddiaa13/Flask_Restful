from service_restful.crud import Crud
from service_restful import db
from flask import request, jsonify


class UserCrud(Crud):

    def post(self):
        users = db.db.users
        username = request.json['username']
        email = request.json['email']

        user_id = users.insert({'username': username, 'email': email})
        new_user = users.find_one({'_id': user_id})

        output = {'username': new_user['username'], 'email': new_user['email']}
        return jsonify({'result': output})

    def get(self):
        users = db.db.users
        output = []

        for user in users.find():
            output.append({'username': user['username'], 'email': user['email']})

        return jsonify({'result': output})


# api.add_resource(HandleUsers, '/HandleUsers')
