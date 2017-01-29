print "This is the server code"


import socket


TCP_IP = raw_input("Enter your IP address (empty string for messaging self)")
if (TCP_IP == ""): TCP_IP = "127.0.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 1024 #This represents the character limit, just chose 1024 because it is a power of 2 and its quite large for my needs

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


while True:
	conn, addr = s.accept()
	print "Connection address: ", addr
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	if (data == "quit"): break
	print "received data: ", data
	conn.send(data) #echo
conn.close()

print "Connection Terminated"
r = raw_input("Press any key to continue")