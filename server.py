import socket
import select
import random

clientList = []

PORT = 5000

HOST = '192.168.178.66'

SOCKET_LIST = []

RECV_BUFFER = 4096 

serversocket = ""

UserList = []

class User():

	def __init__(self, name):
		self.name = name
		self.number = UserList.length

class Pattern():
	def __init__(self):
		mid = random.randint(4,15)
		dis = random.randint(1,mid)
		self.numbers = [mid-dis,mid,mid,mid+dis]
		
		


def startChatServer():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind((HOST, PORT))
    serversocket.listen(10)
    SOCKET_LIST.append(serversocket)

    print ("Server started on port: " + str(PORT))
    print ("IP: " + HOST)

def handleChat():
	ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)

	for sock in ready_to_read:
		if sock == server_socket:
			sockfd, addr = server_socket.accept()
			SOCKET_LIST.append(sockfd)
			clientList.append(sockfd)
			print ("Client: (%s, %s) connected" % addr)
			print (sockfd)

		else:
			try:
				data = sock.recv(RECV_BUFFER)
				if data:
					#Chatt stuff
					pass
				else:
					if sock in SOCKET_LIST:
						SOCKET_LIST.remove(sock)
						print("CLient is offline: " + sock.getpeername())



			except:
				print("CLient is offline: " + sock.getpeername())
				continue


def broadcast(sock, message):
	for socket in SOCKET_LIST:
		if socket != serversocket and socket != sock:
			try:
				socket.send(message)
			except:
				pass


def createPattern():
	pat = Pattern()
	random.shuffle(pat.numbers)
	mes = ""
	for i in pat.numbers:
		mes += i
		mes += "."
	broadcast(serversocket, mes)

	





if __name__ == "__main__":
	startChatServer()

	while 1:
		handleChat()
		createPattern()
		
	server_socket.close()