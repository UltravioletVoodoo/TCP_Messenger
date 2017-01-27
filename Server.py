print "This is the server code"



#The following is sample code from https://wiki.python.org/moin/TcpCommunication
#I intend to use this code as a base to learn about basic socket programming in python


#!/usr/bin/env python

import socket


TCP_IP = raw_input("Enter the IP address (Use 127.0.0.1 for messaging self)")
TCP_PORT = 5005
BUFFER_SIZE = 20 #Normally 1024, but we want a fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print "Connection address: ", addr
while True:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "received data: ", data
	conn.send(data) #echo
conn.close()


r = raw_input("Press any key to continue")