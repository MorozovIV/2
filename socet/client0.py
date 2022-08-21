#!/usr/bin/python
from socket import *
import sys
s = socket(AF_INET,SOCK_STREAM)
s.connect(('10.0.10.200',1234))
s.send( ' '.join(sys.argv[1:]))
print s.recv(2048)