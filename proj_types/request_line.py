from typing import TypedDict
from urllib.parse import ParseResult

from proj_types.method import Method

RequestLine = TypedDict(
    "RequestLine",
    {
        "method": Method,
        "uri": ParseResult,
        "version": str,
    },
)
