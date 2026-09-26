#sender.py


import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)
seq_num = 0
address = ("127.0.0.1", 5000)

#Transfer Stats
total_packets_sent = 0
retransmissions = 0


def reliable_send(sock, data, address, seq_num):

    ack_received = False
    header = (str(seq_num) + "|").encode()
    datapacket = header + data

    while ack_received == False:
        sock.sendto(datapacket, address)
        global total_packets_sent
        total_packets_sent += 1

        try:

            ACKpacket = sock.recvfrom(1024)

            rawReceivedACK = ACKpacket[0]
            receivedACK = rawReceivedACK.decode()
            ackData = receivedACK.split("ACK ", maxsplit=1)
            ackseq_num = int(ackData[1])
            if ackseq_num == seq_num:
                ack_received = True
                print("Sender Received " + ACKpacket[0].decode())
                #print(ACKpacket[1])
                return (seq_num + 1)
            
            
        except TimeoutError:
            ack_received = False
            global retransmissions
            retransmissions += 1
            print("Timeout! Retransmitting packet", seq_num)

file = open("test.txt", "rb")
chunk = file.read(100)

while (len(chunk) > 0):
    seq_num = reliable_send(sock, chunk, address, seq_num)
    chunk = file.read(100)

seq_num = -1
seq_num = reliable_send(sock, chunk, address, seq_num)

file.close()

print("Statistics:")
print("Total Packets Sent: " + str(total_packets_sent))
print("Retransmissions: " + str(retransmissions))


