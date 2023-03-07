from flask_restx import Namespace, Resource
from flask import request

from cource_3.implemented import auth_service

auth_ns = Namespace('auth')

@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        auth_service.create_user(req_json)
        return '', 201

@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email', None)
        password = req_json.get('password', None)
        if None in [email, password]:
            return '', 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens
