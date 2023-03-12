from fast_graphql.connect import client, redis
from fast_graphql.libs.dao import DaoModel
import bcrypt
from fast_graphql.config import Config
from fast_graphql.libs.exception import BaseException
import jwt

db = client.db

class UserHelper:
    def __init__(self) -> None:
        self.dao = DaoModel(db.user, redis)

    def register(self, username, password, avatar="", fullName=""):
        data = {"username": username, "password": bcrypt.hashpw(
            password.encode(), salt=Config.SALT_PW).decode(), "avatar": avatar, "fullName": fullName}
        if self.dao.find_one({"username": "admin"}) is None:
            self.dao.insert_one(data)
            return True
        raise BaseException(message="register fail",
                            status=400, errors=['username existed'])

    def login(self, username, password):
        user = self.dao.find_one({"username": username})
        if user:
            if bcrypt.checkpw(password.encode(), user['password'].encode()):
                access_token = jwt.encode(
                    {'username': user['username']}, key=Config.JWT_SECRET_KEY_ACCESS, algorithm='HS256')
                refresh_token = jwt.encode(
                    {'username': user['username']}, key=Config.JWT_SECRET_KEY_REFRESH, algorithm='HS256')
                return {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
            else:
                raise BaseException(message="login fail", status=400, errors=[
                                    'username or password incorrect'])
        else:
            raise BaseException(message="login fail", status=400, errors=[
                                'username or password incorrect'])

    def get_user_info(self, _token: str):
        payload = jwt.decode(
            _token, key=Config.JWT_SECRET_KEY_ACCESS, algorithms=['HS256'])
        user = self.dao.find_one(payload)
        return user