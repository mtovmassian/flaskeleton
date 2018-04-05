from flask import request
from flask_restful import Resource
from app.middlewares import response
from app.middlewares import auth_guard


class Version(Resource):

    @classmethod
    def set_context(cls, context):
        cls.config = context["config"]

    @auth_guard.login_required(request)
    def get(self):
        try:
            data = {
                "name": self.config.get("server.name"),
                "version": self.config.get("server.version")
            }
            return response.send_200(data)
        except Exception as error:
            return response.send_500(error)
