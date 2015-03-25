#!/usr/bin/python

from PyQt4 import QtCore, QtGui, uic
import sys
from random import randrange
import npcships, choosewords


class Battleships(QtGui.QMainWindow):
	def __init__(self):
		#initialize game window
		super(Battleships, self).__init__()
		self.gameui = uic.loadUi('gameui.ui', self)  #load ui from file
		self.game_started = False
		self.show()
		
		self.gameui.startbutton.clicked.connect(self.game) #starts game
		self.gameui.actionVerlaat_spel.triggered.connect(self.exitgame)
	
	def game(self):
		self.shiplengths = [2,2,3,3,4]			
		self.shiporientation = True 
		self.shiporientation = self.rotateship(self.shiporientation, True) #orientation means direction ship is pointing in,True = Horizontal, False = Vertical
		self.npccoords = npcships.generate(self.shiplengths)
		self.woordenlijst = choosewords.choosewords()
		
		self.gameui.rotateleft.setEnabled(True)
		self.gameui.startbutton.setEnabled(False)	
			
		self.gameui.rotateleft.clicked.connect(lambda: self.rotateship(self.shiporientation, False))
		
	def rotateship(self, shiporientation, returning):
		if returning == False:
			if self.shiporientation == False:
				self.shiporientation = True
			else:
				self.shiporientation = False
			print(self.shiporientation)
		
		if returning == True:
			return self.shiporientation	
				
	def choosecoords(self, gameui, shiplengths): #to do: needs check to see if all ships have been placed
		shipnumber = 1
		message = "Place ship #1" #change message dynamically
		gameui.instructionlabel.setText(message)
			
		#connects all buttons to function that handles input
		for x in range(1,10):
			for y in range(1,10):
				self.coord = gameui.findChild(QtGui.QPushButton, "s" + str(x) + str(y))
				gameui.self.coord.clicked.connect(lambda: inputhandler(shiplengths))
			
	def inputhandler(self, shiplengths):
		ships_placed = 0
		if ships_placed != 5:		
			#checks if coord is an acceptable value
			sendingbutton = sender().objectName() #value is s followed by x and y coordinate
			x = sendingbutton[1]
			y = sendingbutton[2]
			if shiporientation == 0:
				x += 1
			
		

	
	def exitgame(self):
		sys.exit()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	w = Battleships()
	sys.exit(app.exec_())



