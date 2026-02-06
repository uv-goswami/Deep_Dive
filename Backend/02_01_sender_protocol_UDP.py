import socket
import random
import time

#AF(address family)_INET = IPV4 || SOCK_DGRAM(Datagram Ptotocol) = UDP || No Handshake Fire and forget
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)   # is a tuple, combination of IP Address + Port.

prices = ["$101", "$102", "$103", "$104", "$105", "Sell Now"]

for price in prices: 

    if random.random() < 0.5:
        print(f"Dropped packet: {price}")
        continue

    # Introduces latency
    time.sleep(random.uniform(0.01, 0.05))

    #Routing, sending Package using UDP. No connection No handshake
               #Serialization 101 -Encoding converts string to bytecode (using UTF-8)
    sock.sendto(price.encode(), server_address)
    print(f"Sent: {price}")