from socket import *
import time

serverName='***.***.***.***'
serverPort=11995

clientSocket=socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(0,10):
    senttime=time.time()
    message="ping %d %.3fs"%(i+1,senttime)
    try:
        clientSocket.sendto(message.encode(),(serverName,serverPort))
        message,severAddress=clientSocket.recvfrom(2048)
        rtt=time.time()-senttime
        print('Sequence %d: Reply from %s  RTT = %.3fs' % (i + 1, serverName, rtt))
    except Exception as e:
        print('Sequence %d: Request timed out' % (i+1))

clientSocket.close()
