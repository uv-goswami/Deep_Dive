import socket
import json
import time
import random




sockDriver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)

trucks = {
    "truck_id": "001",
    "lat": 5.59,
    "long": 8.23
}


try:
    while True:
        trucks["lat"] += 1
        trucks["long"] += 1

        if random.random() <0.2:
            print("GPS signal Lost")
            time.sleep(1.5)
            continue

        json_string = json.dumps(trucks)

        byte_data = json_string.encode()
        sockDriver.sendto(byte_data, server_address)
        time.sleep(0.9)

except KeyboardInterrupt:
    print("Stopped")

finally:
    sockDriver.close()
