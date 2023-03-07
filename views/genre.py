from flask_restx import Namespace, Resource

from cource_3.dao.model.genre import GenresSchema
from cource_3.implemented import genre_service

genre_ns = Namespace('genre')

@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = GenresSchema(many=True).dump(genres)
        return result, 200

@genre_ns.route('/<int:mid>')
class GenreView(Resource):
    def get(self, mid):
        genre = genre_service.get_one(mid)
        result = GenresSchema().dump(genre)
        return result, 200