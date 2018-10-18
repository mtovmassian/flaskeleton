from flask_restful import Resource
from api.middlewares.rest_response import RESTResponse
from api.config.config import Config


class Version(Resource):

    @classmethod
    def set_context(cls, context):
        cls.config: Config = context["config"]
        cls.logger = context["logger"]

    def get(self):
        try:
            data = {
                "name": self.config.get_app_name(),
                "version": self.config.get_app_version()
            }
            return RESTResponse(data=data).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse(error=str(error)).SERVER_ERROR()
