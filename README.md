# Reliable UDP File Transfer

This project is a simple file transfer porgram built using the foundation of UDP. It takes the idea that UDP doesn't guarantee delivery. It was done by adding sequence numbers, ACKs, timeouts with retransmission, and duplicate detection. 

#  The Mechanics

The sender is able to read the file in 100 byte chunks and it sends a packet at a time. Each packet has its own sequence number. Then the sender waits for an ACK before sending its next packet. If the ACK doesn't arrive before the two second timeout, it resends the packet. 

The receiver keeps tracks of what the next expected sequence number is. If it receives a duplicated packet, it doesn't write the data again and instead sends back the ACK again.

## Packet loss testing

The receiver can simulate random packet and ACK loss using configurable drop rates. I used this to test if the transfer succeeds even if the packets or ACKS are lost. 

## Example

For one test with 5% packet loss and 5% ACK loss:

- Total packets sent: 399
- Retransmissions: 35
- Packets dropped: 19
- ACKs dropped: 16
- Duplicates seen: 16

The resulting file still matched the original file.

## Running

Run the receiver first to open a socket: 'python receiver.py'

Then in another terminal run: 'python sender.py'

The sender uses 'test.txt' and the receiver stores the data in 'result.txt'

## Current weaknesses/limitations

The project currently uses Stop-and-Wait, so only one packet is sent at a time.

Possible future improvements would be using a sliding window, testing over separate machines, and adding more performance measurements.