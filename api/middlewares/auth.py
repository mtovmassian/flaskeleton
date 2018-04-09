"""
    Provides logic to control API access.
"""


import jwt
from datetime import datetime
from datetime import timedelta
from typing import Callable
from api.middlewares import responses as res


ACCESS_TOKEN_NAME = "X-Access-Token"
JWT_SECRET_KEY = "flaskeleton"  # TODO: Change and externalize secret key


def login_required(request) -> Callable:
    """
        Used as a decorator.
        Control user authentication before resource consumption by checking
        JWT token validity.
    """
    def decorator(request_handler: Callable) -> Callable:
        def wrapper(request_context):
            token = extract_token(request)
            if token:
                try:
                    jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
                    return request_handler(request_context)
                except Exception as error:
                    pass
            return res.send_401(error="Unauthorized access")
        return wrapper
    return decorator


def extract_token(request) -> str:
    """
        Extract token from request by checking cookies and headers.
    """
    token = None
    if request.cookies.get(ACCESS_TOKEN_NAME):
        token = request.cookies.get(ACCESS_TOKEN_NAME)
    elif request.headers.get(ACCESS_TOKEN_NAME):
        token = request.headers.get(ACCESS_TOKEN_NAME)
    return token


def set_access_token(infos: any):
    """
        Manage access token response.
    """
    expiration = datetime.utcnow() + timedelta(days=1)
    token = generate_access_token(infos, expiration)
    access_token_cookie = "{cookie_name}={token}; Expires={exp}".format(
        cookie_name=ACCESS_TOKEN_NAME, token=token,
        exp=expiration.strftime("%a, %d %b %Y %H:%M:%S GMT")
    )
    return res.send_200(
        data={"token": token},
        headers={"Set-Cookie": access_token_cookie}
    )


def generate_access_token(infos: any, expiration: int) -> str:
    playload = {**infos, "exp": expiration}
    token = jwt.encode(playload, JWT_SECRET_KEY, algorithm="HS256").decode()
    return token