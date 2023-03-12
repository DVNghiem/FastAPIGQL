from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import load_schema_from_path,\
    snake_case_fallback_resolvers, make_executable_schema

from libs.exception import format_error
import uvicorn
from connect import client
from config import Config

app = FastAPI(debug=True)
client.init_app(app, Config.MONGO_URI)

type_defs = load_schema_from_path('graphql')
from apis import query, mutation
schema = make_executable_schema(
    type_defs,
    [*query, *mutation],
    snake_case_fallback_resolvers
)

app.mount('/graphql', GraphQL(schema=schema,
          debug=True, error_formatter=format_error))

if __name__ == '__main__':
    uvicorn.run(app="main:app", host='0.0.0.0', port=8000, reload=False, log_config='log.ini')
    # uvicorn.run(app="main:app", host='0.0.0.0', port=8000, reload=True)
