from typing import Literal, Optional, TypedDict, TypeGuard, get_args
from urllib.parse import ParseResult, urlparse

from proj_types.response import Response, ResponseBuilder

Method = Literal[
    "OPTIONS",
    "GET",
    "HEAD",
    "POST",
    "PUT",
    "DELETE",
    "TRACE",
]

RequestLine = TypedDict(
    "RequestLine",
    {
        "method": Method,
        "uri": ParseResult,
        "version": str,
    },
)


def is_valid_method(method: str) -> TypeGuard[Method]:
    allowed_methods = get_args(Method)

    if method in allowed_methods:
        return True
    return False


def parse_request_line(
    line: str,
) -> tuple[Optional[RequestLine], Optional[Response]]:
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

    if not is_valid_method(method):
        return (
            None,
            ResponseBuilder()
            .status(405)
            .message(f"Method Not Allowed: {method}")
            .build(),
        )

    # Request-URI can be * | absoluteURI | abs_path | authority
    # server will not support CONNECT / Authority
    uri = urlparse(uri)

    if uri.path == "*" and method != "OPTIONS":
        return (
            None,
            ResponseBuilder()
            .status(400)
            .message("Bad Request: * can only be used with OPTIONS")
            .build(),
        )

    request_line: RequestLine = {"method": method, "uri": uri, "version": http_version}

    return request_line, None


def parse_header(header: str) -> tuple[Optional[dict[str, str]], Optional[Response]]:
    return None, None
