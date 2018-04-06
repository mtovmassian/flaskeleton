from flask_restful import abort


class Response:

    def send_200(self, data=None, headers={}):
        body = {"error": None}
        if data:
            body = {**data, **body}
        return (body, 200, headers)

    def send_400(self, error, data=None, headers={}):
        body = {"error": error}
        if data:
            body = {**data, **body}
        return (body, 200, headers)

    def send_401(self, error, data=None, headers={}):
        body = {"error": error}
        if data:
            body = {**data, **body}
        return (body, 401, headers)

    def send_500(self, error, data=None, headers={}):
        body = {"error": str(error)}
        if data:
            body = {**data, **body}
        return (body, 500, headers)
