import socket
import json
import time


sockOrder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6000)

print("Connecting to Server")
sockOrder.connect(server_address)


order = {
    "ordeer_id": 124,
    "amount": 500
}


try:
    
    json_data = json.dumps(order)

    byte_data = json_data.encode()
    sockOrder.sendall(byte_data)
    print(f"{order}")
    time.sleep(1)

    ack = sockOrder.recv(4096)
    if(ack.decode() == "Order Received"):
        print("Order Received")
        sockOrder.close()


except KeyboardInterrupt:
    print("Stopped")

finally:
    sockOrder.close()
