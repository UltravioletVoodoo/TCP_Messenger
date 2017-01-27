print "This is the server code"


import socket


TCP_IP = raw_input("Enter the IP address (Use 127.0.0.1 for messaging self)")
TCP_PORT = 5005
BUFFER_SIZE = 50 #Normally 1024, but we want a fast response, 50 is the "character limit"

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


r = raw_input("Press any key to continue")