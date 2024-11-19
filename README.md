# UDP communication example

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This repository demonstrates client-server interaction using UDP sockets. It includes two client scripts and one server script that showcase fundamental message sending and receiving functionality.

## Project structure

- **client1.py** and **client2.py**: Client scripts that send messages to the server.
- **server.py**: Server script that processes incoming messages from clients and sends back responses.

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

---