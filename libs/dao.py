from .cache import Cache
from pymongo.collection import Collection
from redis import Redis

class DaoModel(Cache):
    def __init__(self, collection: Collection, redis: Redis) -> None:
        super().__init__(collection, redis)

    def update_one(self, filters, data, bg_job = False):
        if bg_job:
            pass
        else:
            self.collection.update_one(filter=filters, update=data)

    def insert_one(self, data, bg_job = False):
        if bg_job:
            pass
        else:
            return self.collection.insert_one(data)
        
    def find_one(self, filters):
        return self.collection.find_one(filters)
    
    def find_in_cache(self, filters):
        pass