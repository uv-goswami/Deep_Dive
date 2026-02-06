import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
sock.bind(server_address)

print("Bot is listning..............")

while True:
    data, address = sock.recvfrom(4096)


    price = data.decode()

    print(f"Received: {price} from {address}")

    if price == "Sell Now":
        print("selling stocks")
        break