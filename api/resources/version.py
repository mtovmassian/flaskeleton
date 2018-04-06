from flask import request
from flask_restful import Resource
from api.middlewares.auth import Auth
from api.middlewares.response import Response


class Version(Resource):

    res = Response()
    auth = Auth()

    @classmethod
    def set_context(cls, context):
        cls.config = context["config"]
        cls.logger = context["logger"]

    @auth.login_required(request)
    def get(self):
        try:
            data = {
                "name": self.config.get("server.name"),
                "version": self.config.get("server.version")
            }
            return self.res.send_200(data)
        except Exception as error:
            self.logger.error(error)
            return self.res.send_500(error)
