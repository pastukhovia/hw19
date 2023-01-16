from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_movies = user_service.get_all()
        res = UserSchema(many=True).dump(all_movies)
        return res, 200

    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201
