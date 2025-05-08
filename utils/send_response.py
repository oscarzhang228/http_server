from typing import Optional

from http_server_types.response import Response


def send_response(res: Response, http_version: str = "HTTP/1.1") -> Optional[str]:
    # Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF

    return None
