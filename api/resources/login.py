from flask import request
from flask_restful import Resource
from api.middlewares import auth
from api.middlewares import responses as res
import hashlib


class Login(Resource):

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
            # TODO: Remove and implement your own user data access logic >>>>
            username_stored = "flaskeleton"
            password_stored = "603693520ca13d90fc0ff2d13969c1ee"
            user = {
                "username": "flaskeleton",
                "firstname": "flaskeleton",
                "lastname": "flaskeleton"
            }
            # <<<<
            if username == username_stored:
                if hashlib.md5(password.encode()).hexdigest() == password_stored:
                    return auth.set_access_token(infos=user)
            return res.send_400(error="Bad credentials")
        except Exception as error:
            self.logger.error(error)
            return res.send_500(error)
