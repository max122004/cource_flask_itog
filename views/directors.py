from flask_restx import Namespace, Resource

from cource_3.dao.model.director import DirectorsSchema
from cource_3.implemented import director_service

director_ns = Namespace('director')

@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = DirectorsSchema(many=True).dump(directors)
        return result, 200

@director_ns.route('/<int:mid>')
class DirectorView(Resource):
    def get(self, mid):
        director = director_service.get_one(mid)
        result = DirectorsSchema().dump(director)
        return result, 200