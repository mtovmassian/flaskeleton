from flask_restful import Resource
from api.middlewares import response as res


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
            return res.send_200(data)
        except Exception as error:
            self.logger.error(error)
            return res.send_500(error)
