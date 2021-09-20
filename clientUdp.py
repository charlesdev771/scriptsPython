import socket

ip = '127.0.0.1'
port = 7777

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (ip,port)

while True:

    msg = input('>>>: ')
    udp.sendto(msg, dest)
    msg, conn = udp.recvfrom(1024)
    print(msg)
udp.close()