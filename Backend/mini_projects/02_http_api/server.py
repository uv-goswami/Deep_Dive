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

        order_id = json.loads(body)["id"]
        print(json.loads(body)["id"])

        splitting = data.split("\r\n")
        first_line = splitting[0]

        if "POST" in first_line and "/order" in first_line:
            order.id = order_id

        print(order.id)
        print(order_id)

        length = len(body)

        response = (
            f"HTTP/1.1 200 OK\r\n"
            f"Content-type: application/json\r\n"
            f"Content-length: {length}\r\n"
            f"Connection: close\r\n"
            f"\r\n"
            f"{body}"
            )

        connection.send(response.encode())
        



except KeyboardInterrupt:
    print("server stopped")

finally:
    server.close()

