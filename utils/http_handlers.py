import os
from email import message
from typing import Optional
from urllib.parse import ParseResult

from http_server_types.response import Response, ResponseBuilder


def get_data(uri: ParseResult) -> tuple[Optional[str], Optional[Response]]:
    if not os.path.exists(f"/data{uri.path}/data.txt"):
        return (
            None,
            ResponseBuilder()
            .status(404)
            .message(f"Data does not exist at path {uri.path}")
            .build(),
        )

    return None, None
