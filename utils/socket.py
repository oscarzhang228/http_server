import socket
from typing import Optional

from utils.response import Response, ResponseBuilder


def recv_line(conn: socket.socket) -> tuple[str, Optional[Response]]:
    """

    Args:
        sock: TCP socket

    Returns: one line of the message, error as a response if any errors occurred

    """
    try:
        msg = []
        while True:
            nxt_byte = conn.recv(1)

            # handle CRLF
            if nxt_byte == b"\x0d":
                _ = conn.recv(1)
                break

            msg.append(nxt_byte)

        return b"".join(msg).decode(), None
    except Exception as e:
        return (
            "",
            ResponseBuilder()
            .status(500)
            .message(f"Internal Server Error: {e}")
            .build(),
        )
