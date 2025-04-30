import socket

from utils.response_utils import Response
from utils.socket_utils import recv_line

HOST = "localhost"
PORT = 3000


def main():
    print("Starting server")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(0)

        conn, _ = sock.accept()

        msg, err = recv_line(conn)

        if err:
            print(Response().status(500).message("Failed at recv_line"))
            return

        print(msg)
        print()

    pass


if __name__ == "__main__":
    main()
