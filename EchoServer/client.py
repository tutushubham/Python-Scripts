import socket

HOST_add = '127.0.0.1'  
PORT_add = 12345       

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('Connecting to host')
    s.connect((HOST_add, PORT_add))
    print('Connected to host!')
    s.sendall(b'Hi, there... How are you?')
    data = s.recv(100)

print('Received data from the host -', repr(data))