import socket
from urllib.parse import urlparse, parse_qs

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.settimeout(2.0)
server_address = ('localhost', 6000)

request = "https://www.google.com/url?sa=E&source=gmail&q=google.com"

url = urlparse(request)
print(url)

keys = parse_qs(url.query)
domain_list = keys.get('q')
print(f"Domain_list: {keys.get('q')}")

target_domain = domain_list[0]

data = target_domain.encode()
try:
    client_sock.sendto(data, server_address)
    print(f"Requested IP for {request}")
except:
    print("Couldn't send Request")

response, _ = client_sock.recvfrom(4096)
print(f"\nIP for {target_domain} : {response.decode()}")

client_sock.close()
    