# HTTP Server + Client Built in Python

Built to learn how HTTP works and built on top of the BSD socket library’s TCP sockets.

## Features

### Web Server

- **Request Parsing & Response Generation**
  - Full request-line & header parsing
    - Supported Headers:
      - TBD
  - Query-string parsing (`/search?q=python&lang=en`)
  - Response to methods:
    - HEAD: Send headers
    - GET: Send file if it exists
    - POST: Create a new file and write the contents of the request body to it
    - PUT: Overwrite existing file
    - PATCH: Given a range of lines
- **Connection Management**
  - Persistent connections (`keep-alive` / `close`)
  - Socket/read timeouts to prevent hangs
  - Thread-pool worker model for connections

### Web Client

- **Basic Request Sender**
  - Build & send GET, HEAD, POST, PUT, DELETE requests
  - Custom headers & payloads
- **Response Reader**
  - Parse status line, headers, and body
