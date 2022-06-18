from socket import *

HOST = '192.168.50.143'
PORT = 2425

ADDR = (HOST, PORT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock.connect(ADDR)
#head = ''
#a = int(input('>'))
while True:
    data = '1:100:Gogo:192.168.50.143:32:张宽,张宽，张宽，张宽，张宽，张宽'
    sd = data.encode('gbk')
    udpCliSock.sendto(sd, ('192.168.50.143:32', 2425))
    udpCliSock.close()
