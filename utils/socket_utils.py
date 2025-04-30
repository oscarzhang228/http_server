import socket
from typing import Optional


def recv_line(conn: socket.socket) -> tuple[str, Optional[Exception]]:
    """

    Args:
        sock: TCP socket

    Returns: one line of the message, error if it exists

    """
    try:
        msg = []
        while True:
            nxt_byte = conn.recv(1).decode()

            if nxt_byte == "\r":
                # grab the \n as well
                conn.recv(1)
                break

            msg.append(nxt_byte)

        return "".join(msg), None
    except Exception as e:
        return "", e
