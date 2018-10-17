"""
    Provides pre-built HTTP responses.
"""

class RESTResponse:

    def __init__(self, data: dict={}, error: str=None, headers: dict={}):
        self.body = {}
        if data:
            self.body = {**self.body, **data}
        if error:
            self.body["error"] = error
        self.headers = headers

    def OK(self):
        return self.send(200)
    
    def CREATED(self):
        return self.send(201)

    def UNAUTHORIZED(self):
        return self.send(401)

    def FORBIDDEN(self):
        return self.send(403)

    def SERVER_ERROR(self):
        return self.send(500)
    
    def send(self, HTTP_CODE: int):
        self.body["status_code"] = HTTP_CODE
        return (self.body, HTTP_CODE, self.headers)