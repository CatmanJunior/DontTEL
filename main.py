import socket
import sys
import select

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen

import time



PORT = 5000
IP = "192.168.178.94"



clientList = []

startTime = time.time()


sm = ScreenManager()


MessageList = [[],[],[],[]]
UserList = []

class chatMessage():

	def __init__(self, s, r, m):
		self.sender = s
		self.receiver = r
		self.message = m

class User():

	def __init__(self, u):
		self.username = u

	def setUsername(self,u):
		self.username = u



class Pattern():
	def __init__(self):
		mid = random.randint(4,15)
		dis = random.randint(1,mid)
		self.numbers = [mid-dis,mid,mid,mid+dis]
		
		


class ChatScreen(Screen):
	nowTime = NumericProperty(int(time.time()-startTime))
	

	def sendPress(self, *args):
		thisUser.username
		mytextinput = self.ids.my_textinput
		if (mytextinput.text != ""):
			label = self.ids['mylabel']
			newMsg = chatMessage(thisUser.username,"other",mytextinput.text)
			MessageList[0].append(newMsg)
			chatboxtext = ""
			for msg in MessageList[0]:
				chatboxtext += msg.sender + ": " + msg.message + '\n'

			label.text = chatboxtext

			mytextinput.text = ""
			
	def update(self, dt ):
		self.nowTime = 90 - int(time.time()-startTime)

	def backPress(self):
		sm.current = 'gameScreen'

class LoginScreen(Screen):
	def loginPress(self):

		thisUser.setUsername(self.ids.loginName.text)
		print (thisUser.username)
		
		sm.current = 'gameScreen'

class GameScreen(Screen):
	def chatPress(self):
		sm.current = 'chatScreen'	

	def handleCon(self, dt):
		if conn.connected:
			newData = conn.LoadServer()
			if newData:
				typeData = newData[2]
				messageData = newdata[2:-2]

				if typeData == 1:
					conn.logged = True
				if typeData == 2:
					for u in UserList:
						if messageData != u.username:
							newUser = User(messageData)
							
				if typeData == 3:
					pass
				if typeData == 4:
					pass
				if typeData == 5:
					senderData = messageData[0]
					receiverData = messageData[1]
					messageData = messageData[2:]
					
				if typeData == 6:
					pass
				if typeData == 7:
					pass
				if typeData == 8:
					pass
				if typeData == 9:
					pass

class PongApp(App):
	def build(self):
		self.chatScreen = ChatScreen(name='chatScreen')
		self.loginScreen = LoginScreen(name='loginScreen')
		self.gameScreen = GameScreen(name='gameScreen')
		sm.add_widget(self.loginScreen)

		sm.add_widget(self.chatScreen)
		sm.add_widget(self.gameScreen)

		Clock.schedule_interval(self.chatScreen.update, 1.0/60.0)
		Clock.schedule_interval(self.gameScreen.handleCon, 1.0/60.0)

		return sm




class Connexion():

	def __init__(self):
		self.connected = False
		self.logged = False

	def ConnectToServer(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.settimeout(2)

		try:
			self.s.connect((IP,PORT))
		except:
			print("Unable to connect")
		
		self.connected=True
		print ('Connected to server, you can start sending messages!')
		

	def LoadServer(self):
		
		socket_list = [self.s]
		ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [],0)
		
		for sock in ready_to_read:
			
			if sock == self.s:
				
				data = sock.recv(4096)
				if not data: 
					print('Disconnected')
				else:
					return data
					
			
thisUser = User("name")		
conn = Connexion()

if __name__ == '__main__':
	conn.ConnectToServer()
	PongApp().run()
	
	#ConnectToServer()