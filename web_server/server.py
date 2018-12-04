from socket import *

serverPort=11993

serverSocket=socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    print("ready to receive...\n")
    connectionSocket,clientaddr = serverSocket.accept()
    print("connected by",clientaddr)
    try:
        message=connectionSocket.recv(1024)
        message=message.decode()
        filename=message.split()[0]
        f=open(filename)
        data=f.readlines()
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        for i in data:
            connectionSocket.send(i.encode())
    except IOError:
        connectionSocket.send('404 Not Found'.encode())
    
    connectionSocket.close()

serverSocket.close()