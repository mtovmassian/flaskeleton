from flask import request
from flask_restful import Resource
from api.middlewares import auth
from api.middlewares.rest_response import RESTResponse
import hashlib
from datetime import datetime
from datetime import timedelta


class Login(Resource):

    @classmethod
    def set_context(cls, context):
        cls.logger = context["logger"]

    def post(self):
        try:
            body = request.get_json()
            username = body["username"]
            password = body["password"]
            user = self.find_user_by_username(username)
            if user:
                user["is_admin"] = body["is_admin"] if "is_admin" in body.keys() else False
                hashed_password = hashlib.sha512(password.encode()).hexdigest()
                if hashed_password == user["password"]:
                    expiration = datetime.utcnow() + timedelta(days=1)
                    token = auth.generate_access_token(user, expiration)
                    return RESTResponse({"token": token}).OK()
            return RESTResponse({"error":"Bad credentials."}).UNAUTHORIZED()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()

    def find_user_by_username(self, username):
        if (username == "flaskeleton"):
            return {
                "username": "flaskeleton",
                "password": "3a9eb269c59de0d8e0a878acf5195a1ea1ac8bc97e8a3966a692b5328dd3b2c803141a234ff0fedbea0400fd9cd09416477f1fe14ea3b44df496dd841f9c0dbf",
                "first_name": "Flask",
                "last_name": "Eleton"
            }
        return None