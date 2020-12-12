from flask_restful import Resource
from service_restful import api
from service_restful.addResource import addResource
# from service_restful.routes.users.usercrudsql import UserCrud
from service_restful.routes.users.usercrudnosql import UserCrud


class HandleUsers(Resource, UserCrud):

    def post(self):
        newUser = super().post()
        return newUser

    def get(self):
        usersData = super().get()
        return usersData


addResource(api, HandleUsers, '/HandleUsers')
