import socket
import time

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Datagram Acepted"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("Link Available")

# Listen for incoming datagrams
while(True): 
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    #clientMsg = "Message from Client:{}".format(message)
    print("Link busy")
    clientMsg = format(message) 
    print(clientMsg)
    time.sleep(30)
    
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)
    print("Link Available")