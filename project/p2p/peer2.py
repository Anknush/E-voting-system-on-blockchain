import socket

def connect_to_peer(host,port):
    c = socket.socket()
    c.connect((host,port))

def send_msg(data):
    try:
        c.send(bytes(data,'utf-8'))
        if not c.recv(1024).decode()=='ACKD':
            raise ConnectionError

    except KeyboardInterrupt:
        pass
