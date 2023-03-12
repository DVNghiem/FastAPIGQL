from ariadne import ObjectType
import inspect
from typing import Any
from functools import wraps
from .exception import BadRequest, Forbidden, BaseException
from marshmallow import Schema
from utils import message_str
from config import Config
import jwt


class Api:
    def __init__(self, name: str) -> None:
        self._object = ObjectType(name=name)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        _methods = inspect.getmembers(self, predicate=inspect.ismethod)
        for (name, resolve) in _methods:
            if name.startswith('resolve_'):
                self._object.set_field(name=name.replace(
                    'resolve_', ''), resolver=resolve)
        return self._object

    @staticmethod
    def http(
        login_required=False,
        data: Schema = None
    ):
        def _get_token(headers):
            try:
                _type, _token = str(headers['authorization']).split(None, 1)
            except:
                raise BaseException(message="token error",
                                    status=400, errors=['token is required'])
            if _type.lower() != 'bearer':
                return False
            return _token

        def verify_token(headers):
            _token = _get_token(headers)
            if not _token:
                return False
            try:
                jwt.decode(_token, key=Config.JWT_SECRET_KEY_ACCESS,
                           algorithms=['HS256'])
                return True
            except:
                raise BaseException(
                    message="hello", status=403, errors=['token invalid'])

        def internal(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                try:
                    if login_required:
                        if not verify_token(args[2].context['request'].headers):
                            raise BaseException(
                                message="login fail", status=400, errors=["login fail"])
                    if data:
                        _response_validate = data.validate(kwargs)
                        if _response_validate:
                            _error = _response_validate if isinstance(
                                _response_validate, list) else [_response_validate]
                            raise BaseException(
                                message="validate error", status=400, errors=_error)
                    _data = f(*args, **kwargs)
                    return _data
                except Exception as e:
                    if isinstance(e, BaseException):
                        _msg = message_str(msg=e.message, errors=e.errors)
                        if e.status == 403:
                            raise Forbidden(_msg)
                        else:
                            raise BadRequest(_msg)
                    _msg = message_str(msg="Some errors",
                                       errors=["Some errors"])
                    raise BadRequest(_msg)
            return decorated
        return internal
