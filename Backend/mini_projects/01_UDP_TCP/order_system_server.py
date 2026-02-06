import socket
import json
import time


sockOrder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6000)
sockOrder.bind(server_address)
sockOrder.listen(1)
print("waiting for a connection")


try:
    
    connection, address= sockOrder.accept()

    data = connection.recv(4096)
    
    
    byte_data = data.decode()
    json_data = json.loads(byte_data)

    print(f"Order: {json_data}")

    reply = "Order Received"
    connection.send(reply.encode())

except KeyboardInterrupt:
    print("server closed")

