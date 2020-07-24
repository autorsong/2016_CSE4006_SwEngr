from socket import *
import sys

client_socket = socket(AF_INET, SOCK_STREAM)

addr = ()

client_socket.connect(addr)

try:
    data = "asdf"
    client_socket.sendall(data)

    datarecv = client_socket.recv(1024)

    if datarecv:
        print(datarecv)

finally:
    client_socket.close()
