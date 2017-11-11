import socket
import sys
import select

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import random 




class PongGame(Widget):
	pass

class ScatterTextWidget(BoxLayout):
	def sendPress(self, *args):

		mytextinput = self.ids.my_textinput
		if (mytextinput.text != ""):
			label = self.ids['mylabel']
			textList = label.text
			textList += "\n"
			textList += mytextinput.text
			label.text = textList
			mytextinput.text = ""
			print("la")

class PongApp(App):
	def build(self):
		return ScatterTextWidget()

def some_function(*args):
	print ("text changed")




PORT = 5000
IP = "192.168.178.94"

clientList = []


def ConnectToServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	try:
		s.connect((IP,PORT))
	except:
		print("Unable to connect")
		sys.exit()


	print ('Connected to server, you can start sending messages!')
	sys.stdout.write('[Me] ')
	sys.stdout.flush()

	while 1:
		msg = sys.stdin.readline()
		s.send(msg)
		sys.stdout.write('[me] ')
		sys.stdout.flush()
		socket_list = [s]
		ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [],0)

		for sock in ready_to_read:
			
			if sock == s:
				
				data = sock.recv(4096)
				if not data: 
					print('Disconnected')
					sys.exit()
				else:
					
					sys.stdout.write(data)
					sys.stdout.write('[me]');
					sys.stdout.flush()
			
			

if __name__ == '__main__':
	PongApp().run()

	#ConnectToServer()