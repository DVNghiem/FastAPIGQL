from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import load_schema_from_path,\
    snake_case_fallback_resolvers, make_executable_schema
from apis import query, mutation
from libs.exception import format_error
import uvicorn

type_defs = load_schema_from_path('graphql')

schema = make_executable_schema(
    type_defs,
    [*query, *mutation],
    snake_case_fallback_resolvers
)

app = FastAPI(debug=True)
app.mount('/graphql', GraphQL(schema=schema,
          debug=True, error_formatter=format_error))

if __name__ == '__main__':
    # uvicorn.run(app="main:app", host='0.0.0.0', port=8000, reload=True, log_config='log.ini')
    uvicorn.run(app="main:app", host='0.0.0.0', port=8000, reload=True)
