import socket

from http_server_types.header import (EntityHeader, GeneralHeader,
                                      RequestHeader, is_entity_header,
                                      is_general_header, is_request_header)
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

        # Request Line
        msg, err_res = recv_line(conn)

        if err_res:
            print(err_res)
            return

        request_line, err_res = parse_request_line(msg)

        if err_res:
            print(err_res)
            return

        # Headers
        request_headers = list[tuple[RequestHeader, str]]()
        general_headers = list[tuple[GeneralHeader, str]]()
        entity_headers = list[tuple[EntityHeader, str]]()

        while True:
            msg, err_res = recv_line(conn)

            if err_res:
                print(err_res)
                return

            if msg == "":
                break

            header, value = msg.split(":")
            value = value.strip()

            if is_request_header(header):
                request_headers.append((header, value))
            elif is_general_header(header):
                general_headers.append((header, value))
            elif is_entity_header(header):
                entity_headers.append((header, value))
            else:
                print(f"Invalid header {header} and value {value}")


if __name__ == "__main__":
    main()
