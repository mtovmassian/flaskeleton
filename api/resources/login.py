from flask import request
from flask_restful import Resource
from api.middlewares.auth import Auth
from api.middlewares.response import Response
import hashlib


class Login(Resource):

    res = Response()
    auth = Auth()

    @classmethod
    def set_context(cls, context):
        cls.logger = context["logger"]

    def post(self):
        try:
            """
                REPLACE AFTER WITH YOU OWN LOGIN LOGIC
            """
            username = request.json["username"]
            password = request.json["password"]
            username_stored = "flaskeleton"
            password_stored = "603693520ca13d90fc0ff2d13969c1ee"
            if username == username_stored:
                if hashlib.md5(password.encode()).hexdigest() == password_stored:
                    return self.auth.set_access_token()
            return self.res.send_400(error="Bad credentials")
        except Exception as error:
            self.logger.error(error)
            return self.res.send_500(error)
