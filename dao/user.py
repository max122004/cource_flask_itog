from cource_3.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        user = User.query.get(mid)
        return user

    def create_user(self, user):
        user_ent = User(**user)
        self.session.add(user_ent)
        self.session.commit()
        return user_ent

    def get_user_by_username(self, email):
        return self.session.query(User).filter(User.email == email).first()