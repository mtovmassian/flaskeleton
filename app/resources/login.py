from flask import request
from flask_restful import Resource
from app.middlewares.auth import Auth
from app.middlewares.response import Response
import hashlib


class Login(Resource):

    res = Response()
    auth = Auth()

    def post(self):
        try:
            username = request.json["username"]
            password = request.json["password"]
            """
                REPLACE AFTER WITH YOU OWN LOGIN LOGIC
            """
            username_stored = "flaskeleton"
            password_stored = "603693520ca13d90fc0ff2d13969c1ee"
            if username == username_stored:
                if hashlib.md5(password.encode()).hexdigest() == password_stored:
                    token = self.auth.generate_token()
                    data = {"token": token}
                    return self.res.send_200(data)
            return self.res.send_400(error="Bad credentials")
        except Exception as error:
            return self.res.send_500(error)
