#receiver.py

import random
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5000))
expected_seq = 0
streamEnd = False

result_file = open("result.txt", "wb")


#Drop Rates
packetDropRate = 0.4
ackDropRate = 0.4

#Transfer Stats
duplicates_seen = 0 
packets_dropped = 0
ACKS_dropped = 0

while not streamEnd:

    packet = sock.recvfrom(1024)
    #Implemented a random chance for the packet to be dropped
    if(random.random() < packetDropRate):
        print("Packet Dropped")
        packets_dropped += 1
        continue
    rawReceivedData = packet[0]
    splitData = rawReceivedData.split(b"|", maxsplit=1)

    seq_num = int(splitData[0])
    data = splitData[1]
    
    if seq_num != expected_seq:
        if(seq_num == -1):
            if(random.random() < ackDropRate):
                print("ACK Dropped")
                ACKS_dropped += 1
                continue
            returnACK = "ACK " + str(-1)
            enc_ACK = returnACK.encode()
            sock.sendto(enc_ACK, packet[1])
            print("End of File")
            streamEnd = True
            result_file.close()
        else:
            if(random.random() < ackDropRate):
                print("ACK Dropped")
                ACKS_dropped += 1
                continue
            returnACK = "ACK " + str((expected_seq - 1))
            enc_ACK = returnACK.encode()
            sock.sendto(enc_ACK, packet[1])
            duplicates_seen += 1
            print("Duplicate Packet")

    else:
        result_file.write(data)
        result_file.flush()
        if(random.random() < ackDropRate):
            print("ACK Dropped")
            ACKS_dropped += 1
            expected_seq += 1
            continue
        returnACK = "ACK " + str(seq_num)
        enc_ACK = returnACK.encode()
        print("Sequence Number: " + str(seq_num))
        print("Data:", data)
        print("Packet came from:" , packet[1])
        print()
        expected_seq += 1
        sock.sendto(enc_ACK, packet[1])

#This is the testing if the two files are the same

original_file = open("test.txt", "rb")
og_chunk = original_file.read()

copied_file = open("result.txt", "rb")
copied_chunk = copied_file.read()

if(copied_chunk == og_chunk):
    print("Data Transfer Succeeded\n")
else:
    print("Data Transfer Failed\n")

print("Statistics:")
print("Duplicates Seen: " + str(duplicates_seen))
print("Packets Dropped: " + str(packets_dropped))
print("ACKS Dropped: " + str(ACKS_dropped))