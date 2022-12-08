from config import Config
from redis import Redis
from models import Mongo

client = Mongo()

redis = Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT
)