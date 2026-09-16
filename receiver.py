import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5000))
first_packet = True

while True:
    packet = sock.recvfrom(1024)
    rawReceivedData = packet[0]
    receivedData = rawReceivedData.decode()
    splitData = receivedData.split("|", maxsplit=1)

    seq_num = splitData[0]
    data = splitData[1]
    
    if first_packet:
        print("Dropping ACK for packet", seq_num)
        first_packet = False
    else:
        returnACK = "ACK " + str(seq_num)
        enc_ACK = returnACK.encode()
        print("Sequence Number: " + str(seq_num))
        print("Data: " + data)
        print("Packet came from:" , packet[1])
        sock.sendto(enc_ACK, packet[1])