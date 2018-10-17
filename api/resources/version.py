from flask_restful import Resource
from api.middlewares.rest_response import RESTResponse


class Version(Resource):

    @classmethod
    def set_context(cls, context):
        cls.config = context["config"]
        cls.logger = context["logger"]

    def get(self):
        try:
            data = {
                "name": self.config.get("server.name"),
                "version": self.config.get("server.version")
            }
            return RESTResponse(data=data).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse(error=str(error)).SERVER_ERROR()
