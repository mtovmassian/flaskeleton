from flask_restful import abort


class Response:

    def send_200(self, data=None):
        body = {"error": None}
        if data:
            body = {**data, **body}
        return (body, 200)

    def send_400(self, error, data=None):
        body = {"error": error}
        if data:
            body = {**data, **body}
        return (body, 200)

    def send_401(self):
        return abort(401, message="Unauthorized access")

    def send_500(self, error, data=None):
        body = {"error": repr(error)}
        if data:
            body = {**data, **body}
        return (body, 500)
