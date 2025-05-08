from typing import Self, TypedDict, override

Response = TypedDict("Response", {"statusCode": int, "message": str})


class ResponseBuilder:
    def __init__(self):
        self.res = Response({"statusCode": 500, "message": "Internal Server Error"})

    def status(self: Self, statusCode: int) -> Self:
        self.res["statusCode"] = statusCode
        return self

    def message(self: Self, msg: str) -> Self:
        self.res["message"] = msg
        return self

    def build(self: Self) -> Response:
        return self.res

    @override
    def __str__(self: Self) -> str:
        return str(self.res)
