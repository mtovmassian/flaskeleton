from app.middlewares import response


def login_required(request):
    def decorator(request_handler):
        def wrapper(request_context):
            """
                IMPLEMENT YOUR OWN AUTH LOGIC HERE
            """
            # EXAMPLE---
            auth_header = request.headers.get('Authorization')
            if auth_header:
                username, password = auth_header.split(":")
                if username == "flaskeleton" and password == "bone":
                    return request_handler(request_context)
            return response.send_401()
            # ---
        return wrapper
    return decorator
