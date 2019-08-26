#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' 
PORT = 55555      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by Mark 85: ', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            test = b'yes'
            if data == test:
                break
            else:
                msg = input("-> ")
                conn.send(msg.encode())
                
            conn.sendall(data)