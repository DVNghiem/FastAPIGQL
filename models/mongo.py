from pymongo import MongoClient, uri_parser

class Mongo(object):
    def __init__(self) -> None:
        self.db = None
        self.ctx = None
    
    def init_app(self, app, uri, *args, **kwargs):
        parsed_uri = uri_parser.parse_uri(uri)
        database_name = parsed_uri["database"]
        kwargs.setdefault("connect", False)

        self.ctx = MongoClient(*args, **kwargs)
        if database_name:
            self.db = self.ctx[database_name]
        