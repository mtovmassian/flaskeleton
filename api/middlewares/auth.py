"""
    Provides logic to control API access.
"""


import jwt
import re
from datetime import datetime
from datetime import timedelta
from typing import Callable
from api.middlewares.rest_response import RESTResponse


AUTHORIZATION_HEADER = "Authorization"
JWT_SECRET_KEY = "flaskeleton"  # TODO: Change and externalize secret key


def login_required(request) -> Callable:
    """
        Used as a decorator. Control user authentication before resource
        consumption by checking JWT token validity.
    """
    def decorator(request_handler: Callable) -> Callable:
        def wrapper(request_context):
            token = extract_token(request)
            if token:
                playload = decode_playload(token)
                if not isinstance(playload, Exception):
                    return request_handler(request_context)
            return RESTResponse({"error":"Unauthorized access."}).UNAUTHORIZED()
        return wrapper
    return decorator


def admin_only(request) -> Callable:
    """
        Used as a decorator. Control user authentication and user admin
        privillege before resource consumption by checking JWT token validity.
    """
    def decorator(request_handler: Callable) -> Callable:
        def wrapper(request_context):
            token = extract_token(request)
            if token:
                playload = decode_playload(token)
                if not isinstance(playload, Exception) and playload.get("is_admin", False):
                    return request_handler(request_context)
            return RESTResponse({"error":"Restricted access."}).FORBIDDEN()
        return wrapper
    return decorator

def extract_token(request) -> str:
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

def decode_playload(token: str) -> any:
    """
        Decode data from JWT token
    """
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
    except Exception:
        return Exception("TOKEN_CORRUPTION")

def set_access_token(infos: any):
    """
        Manage access token response.
    """
    expiration = datetime.utcnow() + timedelta(days=1)
    token = generate_access_token(infos, expiration)
    # access_token_cookie = "{cookie_name}={token}; Expires={exp}".format(
    #     cookie_name=ACCESS_TOKEN_NAME, token=token,
    #     exp=expiration.strftime("%a, %d %b %Y %H:%M:%S GMT")
    # )
    # headers={"Set-Cookie": access_token_cookie}
    return RESTResponse({"token": token}).OK()

def generate_access_token(infos: any, expiration: int) -> str:
    playload = {**infos, "exp": expiration}
    token = jwt.encode(playload, JWT_SECRET_KEY, algorithm="HS256").decode()
    return token
