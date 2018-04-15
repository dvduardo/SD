
#!/usr/bin/python        # This is client.py file
import socket            # Import socket module
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)      # Create a socket object
host = "localhost" # Get local machine name
port = 12345             # Reserve a port for your service.
server_address = ("localhost",12345)
palavra = True

while palavra:
	msg = raw_input("Digite uma mensagem para o Servidor\n")
	if(msg == 'Close'):
		palavra = False;	
	s.sendto(msg,server_address)

s.close()                  # Close the socket when done
