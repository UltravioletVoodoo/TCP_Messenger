print "This is the client"



#The following is sample code from https://wiki.python.org/moin/TcpCommunication
#I intend to use this code as a base to learn about basic socket programming in python


#!/usr/bin/env python 

import socket


TCP_IP = raw_input("Enter the IP address (Use 127.0.0.1 for messaging self)")
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = raw_input("Enter the message")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data: ", data



r = raw_input("Press any key to continue")