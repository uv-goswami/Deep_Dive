import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)

print("Connecting to server")
sock.connect(server_address)

prices = ["$101", "$102", "$103", "$104", "$105", "Sell Now"]

try:
    for price in prices:
        sock.sendall(price.encode())
        print(f"Sent: {price}")
        time.sleep(1)

finally:
    sock.close()