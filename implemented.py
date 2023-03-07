from cource_3.dao.directors import DirectorDAO
from cource_3.dao.genre import GenreDAO
from cource_3.dao.movie import MovieDAO
from cource_3.dao.user import UserDAO
from cource_3.service.auth import AuthService
from cource_3.service.directors import DirectorService
from cource_3.service.genre import GenreService
from cource_3.service.movie import MovieService
from cource_3.service.user import UserService
from cource_3.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao=movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao=genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao=director_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao=user_dao)

auth_service = AuthService(user_service=user_service)