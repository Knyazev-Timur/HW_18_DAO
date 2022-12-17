from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.directors import DirectorSchema
from app.implemented import directors_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorView(Resource):
    """
    Метод get  для "/directors"
    """
    def get(self):
        directors = directors_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    """
    Метод get
    для "directors/<int:uid>"
    """
    def get(self, uid: int):
        director = directors_service.get_one(uid)
        return director_schema.dump(director), 200
