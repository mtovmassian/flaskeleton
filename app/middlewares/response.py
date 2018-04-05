from flask_restful import abort


def send_200(data):
    body = {"error": None}
    body = {**data, **body}
    return (body, 200)


def send_500(error):
    body = {"error": repr(error)}
    return (body, 500)


def send_401():
    return abort(401, message="Unauthorized access")
