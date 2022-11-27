from libs import Api
from helpers.user import UserHelper
from schemas.user import RegisterSchema, LoginSchema
from utils import get_headers

class UserAPIMutation(Api):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.helper = UserHelper()

    @Api.http(login_required=False, data=RegisterSchema())
    def resolve_register(self, *args,  **kwargs):
        _result = self.helper.register(**kwargs)
        return _result

    @Api.http(login_required=False, data=LoginSchema())
    def resolve_login(self, *args, **kwargs):
        _token = self.helper.login(**kwargs)
        return _token


class UserAPIQuery(Api):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.helper = UserHelper()

    @Api.http(login_required=True)    
    def resolve_getUserInfo(self, *args, **kwargs):
        _request = get_headers(args[1])['authorization'].split()[1]
        _user = self.helper.get_user_info(_request)
        return _user
