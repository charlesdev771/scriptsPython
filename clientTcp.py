import socket

ip = ''
port = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destiny = (ip, port)
sock.connect(destiny)
print(sock.recv(1024))
while True:
    msg = input(">>>: ")
    sock.send(msg)
sock.close()