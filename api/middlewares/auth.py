"""
    Provides logic to control API access.
"""


import jwt
import re
from flask import request
from datetime import datetime
from datetime import timedelta
from typing import Callable
from api.middlewares.rest_response import RESTResponse


AUTHORIZATION_HEADER = "Authorization"
JWT_SECRET_KEY = "flaskeleton"
ALGORITHM = "HS256"


def login_required(request: request) -> Callable:
    """
        Used as a decorator. Control user authentication before resource
        consumption by checking JWT token validity.
    """
    def decorator(request_handler: Callable) -> Callable:
        def wrapper(request_context):
            token = extract_token(request)
            if token:
                payload = decode_payload(token)
                if not isinstance(payload, Exception):
                    return request_handler(request_context)
            return RESTResponse({"error":"Unauthorized access."}).UNAUTHORIZED()
        return wrapper
    return decorator


def admin_only(request: request) -> Callable:
    """
        Used as a decorator. Control user authentication and user admin
        privillege before resource consumption by checking JWT token validity.
    """
    def decorator(request_handler: Callable) -> Callable:
        def wrapper(request_context):
            token = extract_token(request)
            if token:
                payload = decode_payload(token)
                if not isinstance(payload, Exception) and payload.get("is_admin", False):
                    return request_handler(request_context)
            return RESTResponse({"error":"Restricted access."}).FORBIDDEN()
        return wrapper
    return decorator

def extract_token(request: request) -> str:
    """
        Extract token from request by checking cookies and headers.
    """
    token = ""
    if request.cookies.get(AUTHORIZATION_HEADER):
        token = request.cookies.get(AUTHORIZATION_HEADER)
    elif request.headers.get(AUTHORIZATION_HEADER):
        token = request.headers.get(AUTHORIZATION_HEADER)
    return clean_token(token)

def clean_token(token: str) -> str:
    cleaned_token = token
    bearer_name = re.compile(r"^Bearer\s.+")
    if bool(bearer_name.match(token)):
        cleaned_token = token.split(" ")[1]
    return cleaned_token

def decode_payload(token: str) -> any:
    """
        Decode data from JWT token
    """
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        return Exception("TOKEN_CORRUPTION")

def generate_access_token(infos: any, expiration: int) -> str:
    payload = {**infos, "exp": expiration}
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM).decode()
    return token
