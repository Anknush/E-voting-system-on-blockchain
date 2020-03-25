import socket

s = socket.socket()
print('socket created')
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.0.135',9999))

s.listen(5)

print('waiting')

c,addr = s.accept()
print('conn esbd: ', addr)

while True:
    try:
        msg = c.recv(1024).decode()
        print('Pudipeddi mac says:', msg)
        c.send(bytes('ackd','utf-8'))
    except BrokenPipeError:
        pass

