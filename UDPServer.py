from socket import *

serverPort=12000

serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("ready to receive")
while True:
    message,clientAddress=serverSocket.recvfrom(2048)
    message=message.decode().upper()
    serverSocket.sendto(message.encode(),clientAddress)