import socket

ip = "127.0.0.1"
port = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((ip, port))

sock.listen(5)

while True:
    conn, addr = sock.accept()
    str(conn.send((">>> ")))
    masg = conn.recv(1024)
    print("Message: {}".format(msg))
    conn.close()
    break

sock.close()


