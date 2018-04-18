from flask import request
from flask_restful import Resource
from api.middlewares import auth
from api.middlewares import response as res
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
            body = request.json
            username = body["username"]
            password = body["password"]
            # TODO: Remove and implement your own user data access logic >>>>
            username_stored = "flaskeleton"
            password_stored = "603693520ca13d90fc0ff2d13969c1ee"
            is_admin = body["is_admin"] if "is_admin" in body.keys() else False
            user = {
                "username": "flaskeleton",
                "firstname": "flaskeleton",
                "lastname": "flaskeleton",
                "is_admin": is_admin
            }
            # <<<<
            if username == username_stored:
                if hashlib.md5(password.encode()).hexdigest() == password_stored:
                    return auth.set_access_token(infos=user)
            return res.send_400(error="Bad credentials")
        except Exception as error:
            self.logger.error(error)
            return res.send_500(error)
