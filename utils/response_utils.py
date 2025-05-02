from typing import Self, TypedDict, override

Response = TypedDict("Response", {"statusCode": int, "message": str})


class ResponseBuilder:
    def __init__(self):
        self.res = Response({"statusCode": 500, "message": "Internal Server Error"})

    def status(self, statusCode: int) -> Self:
        self.res["statusCode"] = statusCode
        return self

    def message(self, msg: str) -> Self:
        self.res["message"] = msg
        return self

    def build(self) -> Response:
        return self.res

    @override
    def __str__(self) -> str:
        return str(self.res)
