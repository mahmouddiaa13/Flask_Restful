from service_restful.crud import Crud
from service_restful import db
from flask import request, jsonify


class UserCrud(Crud):

    def post(self):
        users = db.db.users
        name = request.json['name']
        email = request.json['email']

        user_id = users.insert({'name': name, 'email': email})
        new_user = users.find_one({'_id': user_id})

        output = {'name': new_user['name'], 'email': new_user['email']}
        return jsonify({'result': output})

    def get(self):
        users = db.db.users
        output = []

        for q in users.find():
            output.append({'name': q['name'], 'email': q['email']})

        return jsonify({'result': output})


# api.add_resource(HandleUsers, '/HandleUsers')
