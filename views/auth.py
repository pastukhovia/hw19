from flask import request
from flask_restx import Resource, Namespace, abort

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthService(Resource):
    def post(self):
        req_json = request.get_json()
        username = req_json.get('username', None)
        password = req_json.get('password', None)

        if None in [username, password]:
            abort(400)

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201


    def put(self):
        req_json = request.get_json()
        refresh_token = req_json.get('refresh_token')
        if refresh_token is None:
            abort(401)

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201
