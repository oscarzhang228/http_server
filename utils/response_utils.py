from typing import Self


class Response:
    def __init__(self):
        self.res = dict[str, str | int]()

    def status(self, statusCode: int) -> Self:
        self.res["statusCode"] = statusCode
        return self

    def message(self, msg: str) -> Self:
        self.res["message"] = msg
        return self
