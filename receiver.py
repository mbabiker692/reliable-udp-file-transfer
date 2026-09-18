#receiver.py

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5000))
expected_seq = 0

while True:
    packet = sock.recvfrom(1024)
    rawReceivedData = packet[0]
    receivedData = rawReceivedData.decode()
    splitData = receivedData.split("|", maxsplit=1)

    seq_num = int(splitData[0])

    
    if seq_num != expected_seq:
        returnACK = "ACK " + str((expected_seq - 1))
        enc_ACK = returnACK.encode()
        sock.sendto(enc_ACK, packet[1])
        print("Duplicate Packet")

    else:
        data = splitData[1]
        returnACK = "ACK " + str(seq_num)
        enc_ACK = returnACK.encode()
        print("Sequence Number: " + str(seq_num))
        print("Data: " + data)
        print("Packet came from:" , packet[1])
        expected_seq += 1
        sock.sendto(enc_ACK, packet[1])