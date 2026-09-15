import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

text = "Hello!"
data = text.encode()

sock.sendto(data, ("127.0.0.1", 5000))

ACKpacket = sock.recvfrom(1024)
print(ACKpacket[0].decode())
print(ACKpacket[1])