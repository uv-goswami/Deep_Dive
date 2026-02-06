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

data = json.dumps(data)
length = len(data)

request = (
    f"POST /order HTTP/1.1\r\n"
    f"Host: localhost\r\n"
    f"Content-type: application/json\r\n"
    f"Content-length: {length}\r\n"
    f"Connection: close\r\n"
    f"\r\n"
    f"{data}"
)


client.send(request.encode())
response = client.recv(4096).decode()
header, body = response.split("\r\n\r\n", 1)
response_body = json.loads(body)
print(header)
print(response_body)

client.close()