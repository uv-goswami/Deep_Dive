import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6000)

client.connect(server_address)
print(f"Connected to {server_address}")

data = {
    "id": 101,
    "amount": 500
}

json_data = json.dumps(data)
byte_data = json_data.encode()
length = len(byte_data)

request = (
    f"POST /order HTTP/1.1\r\n"
    f"Host: localhost\r\n"
    f"Content-type: application/json\r\n"
    f"Content-length: {length}\r\n"
    f"\r\n\r\n"
    f"{byte_data}"
    f"Connection: close\r\n"
)

client.send(request.encode())