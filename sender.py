#sender.py

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

seq_num = 0
text = "Hello!"

datapacket = str(seq_num) + "|" + text

data = datapacket.encode()


ack_received = False
while ack_received == False:
    sock.sendto(data, ("127.0.0.1", 5000))

    try:
        ACKpacket = sock.recvfrom(1024)
        rawReceivedACK = ACKpacket[0]
        receivedACK = rawReceivedACK.decode()
        ackData = receivedACK.split("ACK ", maxsplit=1)
        ackseq_num = int(ackData[1])
        if ackseq_num == seq_num:
            ack_received = True
            print(ACKpacket[0].decode())
            print(ACKpacket[1])
        
        
    except TimeoutError:
        ack_received = False
        print("Timeout! Retransmitting packet", seq_num)

ack_received = False
while ack_received == False:
    sock.sendto(data, ("127.0.0.1", 5000))

    try:
        ACKpacket = sock.recvfrom(1024)
        rawReceivedACK = ACKpacket[0]
        receivedACK = rawReceivedACK.decode()
        ackData = receivedACK.split("ACK ", maxsplit=1)
        ackseq_num = int(ackData[1])
        if ackseq_num == seq_num:
            ack_received = True
            print(ACKpacket[0].decode())
            print(ACKpacket[1])
        
        
    except TimeoutError:
        ack_received = False
        print("Timeout! Retransmitting packet", seq_num)
