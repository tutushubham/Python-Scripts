import socket

HOST = '127.0.0.1' 
PORT = 12345     

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server, is listening on port', PORT)
    conn, addr = s.accept()
    with conn:
        print('Server is connected to', addr)
        while True:
            data = conn.recv(100)
            if not data:
                break
            print('Data from the client',data)
            conn.sendall(data)