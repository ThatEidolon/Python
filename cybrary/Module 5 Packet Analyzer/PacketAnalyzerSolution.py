import struct
import socket
import binascii
import os

def main():
    os.system('cls')
    rawSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    #rawSocket.bind(('10.0.0.3',0))

    receivedPacket = rawSocket.recv(2048)
    
#IP Header... 
    ipHeader=receivedPacket[0:20]
    ipHdr=struct.unpack("!12s4s4s",ipHeader)
    sourceIP = socket.inet_ntoa(ipHdr[0])
    destinationIP=socket.inet_ntoa(ipHdr[2])
    print "Source IP: " +sourceIP
    print "Destination IP: "+destinationIP

#TCP Header...
    tcpHeader=receivedPacket[34:54]
    tcpHdr=struct.unpack("!2s2s16s",tcpHeader)
    sourcePort=socket.inet_ntoa(tcpHdr[0])
    destinationPort=socket.inet_ntoa(tcpHdr[1])
    print "Source Port: " + sourcePort
    print "Destination Port: " + destinationPort

main()
