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
import random




class Game():
	def __init__(self):
		self.state = "start"
		self.pattern = Pattern()
		self.startTime = time.time()
		self.phase = 0



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
	def setNumber(self, n):
		self.number = n
		if n == game.pattern.lowest:
			self.rank = 1
		if n == game.pattern.middle:
			self.rank = 2
		if n == game.pattern.highest:
			self.rank = 3





class Pattern():
	def __init__(self):
		mid = random.randint(4,15)
		dis = random.randint(1,mid)
		self.numbers = [mid-dis,mid,mid,mid+dis]
		self.lowest = mid-dis
		self.middle = mid
		self.highest = mid+dis
		self.distance = dis
		self.names = []


class ChatScreen(Screen):
	
	

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
		for i in range(1,5):
			u = User(self.ids['player' + str(i) + 'name'].text)
			UserList.append(u)
			print(u.username)

		game.state="logged"
		
		sm.current = 'gameScreen'

class GameScreen(Screen):
	
	nowTime = NumericProperty()

	def chatPress(self):
		sm.current = 'chatScreen'	

	def update(self, dt ):

		if game.state == "logged":
			self.ids.player1tag.text = UserList[0].username
			self.ids.player2tag.text = UserList[1].username
			self.ids.player3tag.text = UserList[2].username
			self.ids.player4tag.text = UserList[3].username

		self.nowTime = phaseTime[game.phase] - int(time.time()-game.startTime)

	def newRound(self):
		game.startTime = time.time()
		game.pattern = Pattern()
		random.shuffle(game.pattern.numbers)
		for i in range(4):
			UserList[i].setNumber(game.pattern.numbers[i])

		self.ids.player1number.text = str(UserList[0].number)
		self.ids.player2number.text = str(UserList[1].number)
		self.ids.player3number.text = str(UserList[2].number)
		self.ids.player4number.text = str(UserList[3].number)

		game.phase = 0
		self.ids.roundTag.text = phaseName[game.phase]
		self.ids.answer.text=str(game.pattern.numbers[0]+game.pattern.numbers[1]+game.pattern.numbers[2]+game.pattern.numbers[3])
	
	def nextPhase(self):
		game.phase+=1
		if game.phase == 3:
			game.phase = 2
		game.startTime = time.time()
		self.ids.roundTag.text = phaseName[game.phase]

		

class PongApp(App):
	def build(self):
		self.chatScreen = ChatScreen(name='chatScreen')
		self.loginScreen = LoginScreen(name='loginScreen')
		self.gameScreen = GameScreen(name='gameScreen')
		sm.add_widget(self.loginScreen)

		sm.add_widget(self.chatScreen)
		sm.add_widget(self.gameScreen)


		Clock.schedule_interval(self.gameScreen.update, 1.0/60.0)
		

		return sm

PORT = 5000
IP = "192.168.178.94"

game = Game()
			
thisUser = User("name")		



clientList = []

highHints = [["You have the highest number", ""],
			["the lowest number is:", game.pattern.lowest],
			["You don't have the same number as:", ] ]

phaseName = ["Phase 1: Whatsapp", "Phase 2: Talk", "Phase 3: Choose"]
phaseTime = [120,60,30]
sm = ScreenManager()



UserList = []


if __name__ == '__main__':
	
	PongApp().run()
	
