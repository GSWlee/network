from socket import *

serverName='***.***.***.***'
serverPort=11990

clientSocket =socket(AF_INET,SOCK_STREAM)
message=input("Please enter which page you want?")
clientSocket.connect((serverName,serverPort))
clientSocket.send(message.encode())
modifiedMessage=clientSocket.recv(1024)
while modifiedMessage:
    print(modifiedMessage.decode())
    try:
        modifiedMessage=clientSocket.recv(1024)
    except:
        modifiedMessage=0
clientSocket.close()