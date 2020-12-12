from flask_restful import Resource
from service_restful import api
from service_restful.addResource import addResource
# from service_restful.routes.users.usercrudsql import UserCrud
from service_restful.routes.users.usercrudnosql import UserCrud


class HandleUser(Resource, UserCrud):

    def get(self, user_id):
        usersData = super().getById(user_id)
        return usersData

    def put(self, user_id):
        userUpdated = super().put(user_id)
        return userUpdated

    def delete(self, user_id):
        userDeleted = super().delete(user_id)
        return userDeleted


addResource(api, HandleUser, '/HandleUsers/<int:user_id>')
