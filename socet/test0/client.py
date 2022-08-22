#!/usr/bin/env python
# coding: utf8

import socket
host = '10.0.10.200'
port = 54321
sock = socket.socket()
sock.connect((host, port))
sock.send('hello, world!'.encode())     #.encode() - строку в байты #.decode() - байты в строку

data = sock.recv(1024).decode()
sock.close()

print(data)