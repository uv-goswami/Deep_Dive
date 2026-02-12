import socket
import json


RECORDS = {
    "delhiery.com": "1.2.3.4",
    "google.com": "8.8.8.8"
}


server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 6000)
server_sock.bind(server_address)

print(f"Connected at {server_address}")


while True:
    data, address = server_sock.recvfrom(4096)
    request = data.decode()

    print(request)

    

    response = RECORDS.get(request)

    if response is None:
        print("Recursion required...")
        response = "0.0.0.0"

    
    print(response)

    server_sock.sendto(response.encode(), address)

