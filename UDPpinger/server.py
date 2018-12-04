from socket import *
import random

serverPort=11995

serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("ready to receive")
while True:
    rand = random.randint(0, 10)
    message,clientAddress=serverSocket.recvfrom(2048)
    message=message.decode().upper()
    if rand<4:
       continue
    serverSocket.sendto(message.encode(),clientAddress)