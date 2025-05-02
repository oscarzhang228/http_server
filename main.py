import socket

from utils.parsers import parse_request_line
from utils.socket import recv_line

HOST = "localhost"
PORT = 3000


def main():
    print("Starting server")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(0)

        conn, _ = sock.accept()

        msg, err_res = recv_line(conn)

        if err_res:
            print(err_res)
            return

        request_line, err_res = parse_request_line(msg)

        if err_res:
            print(err_res)
            return


if __name__ == "__main__":
    main()
