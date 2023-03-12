from pymongo.collection import Collection
from redis import Redis
from bson import json_util


class Cache:
    def __init__(self, collection: Collection, redis: Redis) -> None:
        self.collection = collection
        self.redis = redis

    def get_key(self, filters: dict) -> str:
        _filter_key = list(filters.keys())
        _filter_key.sort()
        _key = [f'{i}:{filters[i]}' for i in _filter_key]
        return '_'.join(_key)

    def set(self, key: str, value: dict):
        if value is None:
            value = {}
        value = json_util.dumps(value)
        self.redis.set(key, value)

    def find_with_filter(self, filers):
        _key = self.get_key(filers)
        return self.redis.get(_key)
