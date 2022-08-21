 #!/usr/bin/python
from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
host = "10.0.10.200"
port = 1234
s.bind(('10.0.10.200',1234))
s.listen(5)
while 1 :
    print('server start')
    conn, addr = s.accept()
    data = conn.recv(1024)
    conn.send(data+data)
# print('server stop')