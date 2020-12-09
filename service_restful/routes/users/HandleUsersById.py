from flask_restful import Resource
from service_restful import api
from service_restful.usercrudsql import UserCrud


class HandleUser(Resource):
    def get(self, user_id):
        userCrud = UserCrud()
        usersData = userCrud.getById(user_id)
        return usersData

    def put(self, user_id):
        userCrud = UserCrud()
        userUpdated = userCrud.put(user_id)
        return userUpdated

    def delete(self, user_id):
        userCrud = UserCrud()
        userDeleted = userCrud.delete(user_id)
        return userDeleted


api.add_resource(HandleUser, '/HandleUsers/<int:user_id>')
