from typing import Optional, TypedDict
from urllib.parse import ParseResult, urlparse

from utils.response_utils import Response, ResponseBuilder

ALLOWED_METHODS = set[str](
    [
        "GET",
        "HEAD",
        "POST",
        "PUT",
        "DELETE",
        "TRACE",
    ]
)

RequestLine = TypedDict(
    "RequestLine",
    {method: Literal[ALLOWED_METHODS], uri: ParseResult, version: str},
)


def parse_request_line(
    line: str,
) -> tuple[Optional[dict[str, str]], Optional[Response]]:
    """

    Args:
        line: request line

    Returns: message denoting which part of the request line is invalid

    """

    parts = line.split(" ")

    if len(parts) != 3:
        return None, (
            ResponseBuilder()
            .status(400)
            .message(
                "Bad Request: Request line must consist of 'METHOD Request-URI HTTP-Version'"
            )
            .build()
        )

    method, uri, http_version = parts

    if method not in ALLOWED_METHODS:
        return (
            None,
            ResponseBuilder()
            .status(405)
            .message(f"Method Not Allowed: {method}")
            .build(),
        )

    # Request-URI can be * | absoluteURI | abs_path | authority
    # server will not support CONNECT and thus will not support authority
    uri = urlparse(uri)
    print(method, uri, http_version)

    request_line = dict[str, str]

    return None, None
