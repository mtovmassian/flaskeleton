import jwt
from datetime import datetime
from datetime import timedelta
from app.middlewares.response import Response


class Auth:

    res = Response()

    def login_required(self, request):
        def decorator(request_handler):
            def wrapper(request_context):
                """
                    REPLACE AFTER YOUR OWN AUTH LOGIC
                """
                token = request.headers.get('Authorization')
                if token:
                    try:
                        secret_key = "flaskeleton"
                        jwt.decode(token, secret_key, algorithms=['HS256'])
                        return request_handler(request_context)
                    except Exception as error:
                        pass
                return self.res.send_401()
            return wrapper
        return decorator

    def generate_token(self):
        """
            REPLACE AFTER WITH YOUR OWN TOKEN GENERATION LOGIC
        """
        secret_key = "flaskeleton"
        user = {
            "username": "flaskeleton",
            "firstname": "flaskeleton",
            "lastname": "flaskeleton"
        }
        token_expiration = datetime.utcnow() + timedelta(days=1)
        playload = {**user, "exp": token_expiration}
        token = jwt.encode(playload, secret_key, algorithm='HS256').decode()
        return token
