import base64
import calendar
import datetime
import hashlib

import jwt

from cource_3.constants import SECRET_KEY, ALGORITHM, PWD_HASH_SALT, PWD_HASH_ITERATIONS


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service


    def create_user(self, user):
        return self.user_service.create_user(user)

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_user_by_username(email)

        # if not user:
        #     raise Exception()

        # if not is_refresh:
        #     # проверка совпадения паролей
        #     if not self.user_service.compare_passwords(user.password, password):
        #         raise Exception()

        data = {
            "name": user.name,
            "surname": user.surname
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }