import socket
import json

class order:
    id = 0
    amount = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 6000)
server.bind(server_address)
server.listen(1)
print("waiting for a connection")



try: 
    while True:
        connection, address = server.accept()

        byte_data = connection.recv(4096)
        data = byte_data.decode()
        print(data)

        try:
            header, body = data.split("\r\n\r\n", 1)
        except ValueError:
            body = ""

        



except KeyboardInterrupt:
    print("server topped")

finally:
    server.close()

