from flask_restx import Namespace, Resource

from cource_3.dao.model.user import UserSchema
from cource_3.implemented import user_service

user_ns = Namespace('user')


@user_ns.route('/<int:mid>')
class UserView(Resource):
    def get(self, mid):
        user = user_service.get_one(mid)
        result = UserSchema().dump(user)
        return result, 200

    def patch(self, mid):
        pass

    def put(self, mid):
        pass