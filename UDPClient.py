from socket import *

serverName='***.***.***.***'
serverPort=12000

clientSocket =socket(AF_INET,SOCK_DGRAM)
message="fuch computer network!!"
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()