# HTTP Server + Client Built in Python

Built to learn how HTTP works and built on top of the BSD socket library’s TCP sockets.

## Features

### Web Server

#### Request Parsing

- Following [RFC 2616, Section 5](https://datatracker.ietf.org/doc/html/rfc2616#section-5)

  **Parts**

  - [ ] Request-Line
  - [ ] General-Headers
  - [ ] Request-Headers
  - [ ] Entity-Headers
  - [ ] Query Params

### Future

- connection management (one main listener thread and worker threads)
  - then the Connection header can be respected
- web requester
