from cource_3.dao.model.director import Directors


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        director = Directors.query.all()
        return director

    def get_one(self, mid):
        director = Directors.query.get(mid)
        return director
