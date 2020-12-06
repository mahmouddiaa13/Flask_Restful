from flask_restful import Resource
from service_restful import api
from service_restful.usercrud import UserCrud


class HandleUsers(Resource):

    def post(self):
        userCrud = UserCrud()
        newUser = userCrud.post()
        return newUser

    def get(self):
        userCrud = UserCrud()
        usersData = userCrud.get()
        return usersData


api.add_resource(HandleUsers, '/HandleUsers')
