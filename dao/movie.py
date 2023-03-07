from cource_3.dao.model.movie import Movies


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movie = Movies.query.all()
        return movie

    def get_one(self, mid):
        movie = Movies.query.get(mid)
        return movie