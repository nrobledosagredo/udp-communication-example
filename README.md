# UDP communication example

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This repository demonstrates client-server interaction using UDP sockets. It includes two client scripts and one server script that showcase fundamental message sending and receiving functionality. Created as part of a learning project to explore UDP communication.

## Project structure

- **client1.py**: Client script that sends messages to the server.
- **client2.py**: Another client script that sends messages to the server.
- **server.py**: Server script that processes incoming messages and sends responses.

## How to run

1. Start the server:

```bash
python server.py
```

2. Launch the client scripts in separate terminal windows:

```bash
python client1.py
python client2.py
```

The server will process messages sent by the clients and provide appropriate responses.
