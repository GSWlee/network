from socket import *

serverPort=11999

serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("ready to recieve")
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).upper()
    sentence=sentence.upper()
    connectionSocket.send(sentence.encode())
    connectionSocket.close()
