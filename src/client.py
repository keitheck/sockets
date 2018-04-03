import socket
import sys

infos = socket.getaddrinfo('127.0.0.1', 3000)

stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

client = socket.socket(*stream_info[:3])

client.connect(stream_info[-1])

message = "test message from client"

client.sendall(message.encode('utf8'))

buffer_length = 2048

message_complete = False

while not message_complete:
    part = client.recv(buffer_length)
    print('Echoed from server.py => {}'.format(part.decode('utf8')))
    if len(part) < buffer_length:
        break

message = "close"

client.sendall(message.encode('utf8'))

buffer_length = 2048

message_complete = False

while not message_complete:
    part = client.recv(buffer_length)
    print('Echoed from server.py => {}'.format(part.decode('utf8')))
    if len(part) < buffer_length:
        break

client.close()        