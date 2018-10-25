from flask_restful import Resource
from api.middlewares.rest_response import RESTResponse
from api.config.config import Config
import os


class Version(Resource):

    def __init__(self, logger):
        self.logger = logger

    def get(self):
        try:
            config = Config(os.environ.get("config_profile"))
            data = {
                "name": config.get_app_name(),
                "version": config.get_app_version()
            }
            return RESTResponse(data).OK()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()
