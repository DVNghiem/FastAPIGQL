from libs import Api


class HelloQuery(Api):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    @Api.http()
    def resolve_hello(self, object, info):
        return "hello query"
