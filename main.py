import socket

from http_server_types.header import (is_entity_header, is_general_header,
                                      is_request_header)
from utils.parsers import parse_request_line
from utils.socket import recv_line

HOST = "localhost"
PORT = 3000


def main():
    print("Starting server")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(0)

        while True:
            conn, _ = sock.accept()
            print("Connected")

            # Request Line
            with conn:
                msg, err_res = recv_line(conn)

                if err_res:
                    print(err_res)
                    return

                request_line, err_res = parse_request_line(msg)

                if err_res:
                    print(err_res)
                    return

                # Headers
                request_headers = dict[str, str]()
                general_headers = dict[str, str]()
                entity_headers = dict[str, str]()

                while True:
                    msg, err_res = recv_line(conn)

                    if err_res:
                        print(err_res)
                        return

                    if msg == "":
                        break

                    partition_idx = msg.find(":")
                    header = msg[0:partition_idx]
                    # add 1 to skip one whitespace
                    value = msg[partition_idx + 1 : len(msg)]

                    if is_request_header(header):
                        request_headers[header] = value
                    elif is_general_header(header):
                        general_headers[header] = value
                    elif is_entity_header(header):
                        entity_headers[header] = value
                    else:
                        print(f"Invalid header {header} and value {value}")

                # Request Body
                if "Content-Length" in entity_headers:
                    body = conn.recv(int(entity_headers["Content-Length"]))
                    print(body)


if __name__ == "__main__":
    main()
