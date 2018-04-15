import socket            # Import socket module
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,)      # Create a socket object
#local machine name

server_address = ('localhost', 12345)
s.bind(('localhost', 12345))     # Bind to the port

palavra = True
while palavra:
	msg, addr = s.recvfrom(1024)  # Establish connection with client.
	print "Got msg:",msg,"from", addr
	if msg == 'Close':
		palavra=False
s.close()              # Close the connection
print "Servidor ",addr,"fechou"
