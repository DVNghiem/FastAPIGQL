import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PROJECT_NAME = 'graphql'
    MONGO_URI = os.getenv('MONGO_URI')
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    SALT_PW = os.getenv('SALT_PW', '').encode()
    JWT_SECRET_KEY_ACCESS = os.getenv('JWT_SECRET_KEY_ACCESS', '')
    JWT_SECRET_KEY_REFRESH = os.getenv('JWT_SECRET_KEY_REFRESH', '')
