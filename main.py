import socket
import sys
import select

PORT = 5000
IP = "192.168.178.66"

ClientList = []


def ConnectToServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	try:
		s.connect((IP,PORT))
	except:
		print("Unable to connect")
		sys.exit()


	print ('Connected to server, you can start sending messages!')


ConnectToServer()