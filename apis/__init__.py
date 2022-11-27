from .hello import HelloQuery
from .user import UserAPIMutation, UserAPIQuery

query = [HelloQuery('Query')(), UserAPIQuery('Query')()]
mutation = [UserAPIMutation('Mutation')()]