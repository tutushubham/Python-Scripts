import socket
import threading
import time

tlock=threading.Lock()
shutdown=False

def receiving(name,sock):
    while not shutdown:
        try:
            tlock.acquire()
            while True:
                data,addr=sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tlock.release()

host='192.168.44.1'
port=0

server=('192.168.44.1',8000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

s.setblocking(0)

rt=threading.Thread(target=receiving,args=("RecvThread",s))
rt.start()

alias=raw_input("name :")
message=raw_input(alias+"->")

while message!='q':
    if message!='':
        s.sendto(alias+": "+message,server)
    tlock.acquire()
    message=raw_input(alias+"->")
    tlock.release()
    time.sleep(0.2)
    
shutdown=True
st.join()
s.close()
