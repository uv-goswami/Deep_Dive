import socket


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('Localhost', 10000)
server_sock.bind(server_address)

server_sock.listen(1)
print(f"Server is listning")

while True:
    connection, client_address =server_sock.accept()
    try:
        print(f"Connected to {client_address}")

        data = connection.recv(4096)
        if not data:
            break

        print(f"received {data.decode()}")

    finally:
        connection.close()