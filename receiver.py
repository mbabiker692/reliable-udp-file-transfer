import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5000))

packet = sock.recvfrom(1024)

returnACK = "ACK"
enc_ACK = returnACK.encode()

print(packet[0].decode())
print(packet[1])

sock.sendto(enc_ACK, (packet[1]))