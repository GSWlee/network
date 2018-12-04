from socket import *

serverName='***.***.***.***'
serverPort=11996

clientSocket =socket(AF_INET,SOCK_STREAM)
message="fuck computer network!!"
clientSocket.connect((serverName,serverPort))
clientSocket.send(message.encode())
modifiedMessage=clientSocket.recv(1024)
print(modifiedMessage.decode())
clientSocket.close()