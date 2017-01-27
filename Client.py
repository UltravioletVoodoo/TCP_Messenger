print "This is the client"


import socket


TCP_IP = raw_input("Enter the IP address (Use 127.0.0.1 for messaging self)")
TCP_PORT = 5005
BUFFER_SIZE = 1024

while (True):
	MESSAGE = raw_input("Enter the message")
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)
	
	if (MESSAGE == "quit"): break
	data = s.recv(BUFFER_SIZE)
	print data


s.close()

print "Connection Terminated"
r = raw_input("Press any key to continue")