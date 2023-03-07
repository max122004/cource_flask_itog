import base64
import hashlib
import hmac

from cource_3.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def get_one(self, mid):
        return self.user_dao.get_one(mid)

    def get_user_by_username(self, email):
        return self.user_dao.get_user_by_username(email)

    def generate_user_password(self, password):
        hash_digest = self.get_hash(password)
        return base64.b64encode(hash_digest)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def create_user(self, user):
        user['password'] = self.get_hash(user['password'])
        return self.user_dao.create_user(user)

    def compare_passwords(self, password_hash, other_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            self.get_hash(other_password)
        )