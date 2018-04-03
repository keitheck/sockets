import socket
import datetime

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP
)

address = ('127.0.0.1', 3000)

sock.bind(address)

sock.listen(1)

print('--- Starting server on port 3000 at {} ---'.format(datetime.datetime.today()))

buffer_lenth = 2048

message_complete = False

try:
    conn, addr = sock.accept()

    while not message_complete:
        part = conn.recv(buffer_lenth)
        message = part.decode('utf8')
        if not part:
            break
        conn.sendall(part)
        print('Message received at: {}'.format(datetime.datetime.today()))
        
        print('Echoed => ' + message)

    print('--- Stopping server on port 3000 at {} ---'.format(datetime.datetime.today())) 
    
    if message == 'close':
        """playing around, if message is close, run shutdown command"""
        conn.close()       

except KeyboardInterrupt:
    print(' => exit server')
