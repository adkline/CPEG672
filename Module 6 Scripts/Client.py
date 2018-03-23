#!/usr/bin/env python
import socket, random, binascii
from Crypto.PublicKey import RSA

gen_key = RSA.generate(2048, e = 65537)

public_key = gen_key.publickey().exportKey("PEM") 
private_key = gen_key.exportKey("PEM") 


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = public_key
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
 
print "received data:", data