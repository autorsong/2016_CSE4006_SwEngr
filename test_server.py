from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 8021
addr = (host, port)

server_socket.bind(addr)
server_socket.listen(10)

while True:
    print("waiting for connection..")
    count = 0

    connection, conn_addr = server_socket.accept()

    try:
        data = connection.recv(1024)
        if data:
            print('recv: %s %d' % data % count)
            connection.sendall(data * 2)

    finally:
        connection.close()
