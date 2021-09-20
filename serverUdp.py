import socket 

ip = ''
port = 7777

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origin = (ip, port)
udp.bind(origin)
while True:
    msg, client = udp.recvfrom(1024)
    print(client[0], msg)
    if msg:
        try:
            result = socket.gethostbyname(msg.strip())
        except Exception as error:
            result = str(error)
        udp.sendto(result+'\n',client)
udp.close()