import socket
from typing import Optional

from http_server_types.response import Response, reason_phrases


def send_response(
    conn: socket.socket, res: Response, http_version: str = "HTTP/1.1"
) -> Optional[str]:
    status_line = (
        f"{http_version} {res["statusCode"]} {reason_phrases[res["statusCode"]]}\r\n"
    )

    conn.sendall(status_line.encode())

    return None
