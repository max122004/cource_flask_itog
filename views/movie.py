from flask_restx import Resource, Namespace

from cource_3.dao.model.movie import MoviesSchema
from cource_3.implemented import movie_service

movie_ns = Namespace('movie')

@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        movies = movie_service.get_all()
        result = MoviesSchema(many=True).dump(movies)
        return result, 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        result = MoviesSchema().dump(movie)
        return result, 200