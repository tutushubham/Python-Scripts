#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  
PORT = 55555      

client_socket = socket.socket()  # instantiate
client_socket.connect((HOST, PORT))  # connect to the server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, Client. Welcome to Stark Industries Secure Server.')
    message = input(" -> ")
    client_socket.send(message.encode())
    data = s.recv(1024)
    print(data)
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")

print('Received', repr(data))