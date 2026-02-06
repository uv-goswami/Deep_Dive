import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('www.google.com', 80)

client.connect(server_address)

request = (
    f"GET / HTTP/1.1\r\n"
    f"Host: www.google.com\r\n"
    f"Connection: close\r\n"
    f"\r\n"
)

client.send(request.encode())

receive_data = b""

while True:
    chunk = client.recv(4096)
    if not chunk : break
    receive_data += chunk

print(receive_data.decode())
