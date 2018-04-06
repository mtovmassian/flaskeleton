import jwt
from datetime import datetime
from datetime import timedelta
from api.middlewares.response import Response


class Auth:

    res = Response()

    def login_required(self, request):
        def decorator(request_handler):
            def wrapper(request_context):
                """
                    REPLACE AFTER WITH YOUR OWN AUTH LOGIC
                """
                token = request.cookies.get("X-Access-Token")
                if token:
                    try:
                        secret_key = "flaskeleton"
                        jwt.decode(token, secret_key, algorithms=['HS256'])
                        return request_handler(request_context)
                    except Exception as error:
                        pass
                return self.res.send_401(error="Unauthorized access")
            return wrapper
        return decorator

    def set_access_token(self):
        expiration = datetime.utcnow() + timedelta(days=1)
        token = self.generate_access_token(expiration)
        x_access_token_cookie = "X-Access-Token={token}; Expires={exp}".format(
            token=token, exp=expiration.strftime("%a, %d %b %Y %H:%M:%S GMT")
        )
        return self.res.send_200(
            data={"token": token},
            headers={"Set-Cookie": x_access_token_cookie}
        )

    @staticmethod
    def generate_access_token(expiration):
        """
            REPLACE AFTER WITH YOUR OWN TOKEN GENERATION LOGIC
        """
        secret_key = "flaskeleton"
        user = {
            "username": "flaskeleton",
            "firstname": "flaskeleton",
            "lastname": "flaskeleton"
        }
        playload = {**user, "exp": expiration}
        token = jwt.encode(playload, secret_key, algorithm='HS256').decode()
        return token
