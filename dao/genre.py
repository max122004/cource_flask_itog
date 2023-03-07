from cource_3.dao.model.genre import Genres


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = Genres.query.all()
        return genres

    def get_one(self, mid):
        genre = Genres.query.get(mid)
        return genre


