from pymongo import MongoClient
from config import Config
from redis import Redis

db = MongoClient(Config.MONGO_URI)[Config.PROJECT_NAME]
redis = Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT
)