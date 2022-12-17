from flask import request
from flask_restx import Resource, Namespace
from app.implemented import genre_service

from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreView(Resource):
    """
    Метод get для "/genres"
    """
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    """
    Метод
    для "genres/<int:uid>"
    """
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

