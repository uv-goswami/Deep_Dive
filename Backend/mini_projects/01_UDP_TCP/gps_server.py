import socket
import json


sockGPS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 5000)

sockGPS.bind(server_address)

print(f"Server Listining at {server_address}")


try:
    while True:
        data, address = sockGPS.recvfrom(4096)  
        json_data = data.decode()
        truck_gps = json.loads(json_data)
        print(f"Address {truck_gps["truck_id"], truck_gps["lat"], truck_gps["long"]}")
except KeyboardInterrupt:
    print("stoping the seerver")
finally:
    sockGPS.close()
    print("server closed")



