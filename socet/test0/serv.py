#!/usr/bin/env python
# coding: utf8

import socket
host = '10.0.10.200'
port = 54321
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', host)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send('Получено'.encode())

conn.close()