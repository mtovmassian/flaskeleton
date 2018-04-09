"""
    Provides pre-built HTTP responses.
"""


def send_200(data=None, headers={}):
    body = {"error": None}
    if data:
        body = {**data, **body}
    return (body, 200, headers)


def send_400(error, data=None, headers={}):
    body = {"error": error}
    if data:
        body = {**data, **body}
    return (body, 200, headers)


def send_401(error, data=None, headers={}):
    body = {"error": error}
    if data:
        body = {**data, **body}
    return (body, 401, headers)


def send_500(error, data=None, headers={}):
    body = {"error": str(error)}
    if data:
        body = {**data, **body}
    return (body, 500, headers)
