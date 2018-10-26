from flask import request
from flask_restful import Resource
from api.models import DB
from api.middlewares import auth
from api.middlewares.rest_response import RESTResponse
from api.models.user import User
import hashlib
from datetime import datetime
from datetime import timedelta
from typing import Dict


class Login(Resource):

    def __init__(self, logger, db: DB):
        self.logger = logger
        self.db = db

    def post(self) -> None:
        try:
            body = request.get_json()
            username = body["username"]
            password = body["password"]
            user: User = self.db.find_user_by_username(username)
            if user:
                hashed_password = hashlib.sha512(password.encode()).hexdigest()
                user_payload = {
                    "username": user.username, "first_name": user.first_name, "last_name": user.last_name, "is_admin": user.is_admin
                }
                if hashed_password == user.password:
                    expiration = datetime.utcnow() + timedelta(days=1)
                    token = auth.generate_access_token(user_payload, expiration)
                    return RESTResponse({"token": token}).OK()
            return RESTResponse({"error":"Bad credentials."}).UNAUTHORIZED()
        except Exception as error:
            self.logger.error(error)
            return RESTResponse({"error":str(error)}).SERVER_ERROR()