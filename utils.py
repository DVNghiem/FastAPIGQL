import json
from graphql import GraphQLResolveInfo

def message_str(msg:str, errors: list):
    return json.dumps({"msg": msg, "errors": errors})

def get_headers(info:GraphQLResolveInfo):
    return info.context['request'].headers
