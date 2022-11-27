from graphql import GraphQLError
import json


class BaseException(Exception):
    def __init__(self, message: str = "Base exception", status=400, errors=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
        self.status = status
        self.errors = errors


class BadRequest(GraphQLError):
    def __init__(self, message: str = "Bad request", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.message = message


class Forbidden(GraphQLError):
    def __init__(self, message: str = "Forbidden exception", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.message = message


def format_error(error: GraphQLError,  *args, **kwargs):
    formatted = json.loads(error.message.replace("'", '"'))
    return formatted
