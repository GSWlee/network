from socket import *
import base64

host='smtp.163.com'
port=25
endmsg = "\r\n.\r\n"

user=base64.b64encode(b'************@163.com').decode() + '\r\n'
password=base64.b64encode(b'password').decode()+'\r\n'


clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((host,port))
ans=clientSocket.recv(2048)


if ans[:3]!=b'220':
    print('220 reply not received from server.')

heloCommand = 'HELO ZHIKAI\r\n'
clientSocket.send(heloCommand.encode())
recv=clientSocket.recv(2048)
print(recv.decode())
if recv[:3]!=b'250':
    print('250 reply not received from server.'.encode())

clientSocket.send('AUTH LOGIN\r\n'.encode())
recv=clientSocket.recv(2048).decode()
print(recv)
clientSocket.send(user.encode())
recv=clientSocket.recv(2048)
print(recv)
clientSocket.send(password.encode())
recv=clientSocket.recv(2048)
print(recv)

mailFrom = 'MAIL FROM: <*********@163.com>\r\n'
clientSocket.send(mailFrom.encode())
recv=clientSocket.recv(2048)
print('a',recv)
recvTo = 'RCPT TO:<*********@qq.com>\r\n'
clientSocket.send(recvTo.encode())
recv=clientSocket.recv(2048)
print('b',recv)
clientSocket.send('DATA\r\n'.encode())
recv=clientSocket.recv(2048)
print('c',recv)
clientSocket.send('From:*****163.com\r\n'.encode())
clientSocket.send('To:*********@qq.com\r\n'.encode())
clientSocket.send('Subject:LALALA'.encode())
clientSocket.send('Content-Type:text/plain\r\n'.encode())
clientSocket.send('\r\n GREATE COMPUTER NETWORK'.encode())
clientSocket.send(endmsg.encode())
recv=clientSocket.recv(2048)
print('h',recv)
clientSocket.send('QUIT\r\n'.encode())

clientSocket.close()