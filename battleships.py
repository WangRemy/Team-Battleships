#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, uic
import sys
from random import randrange, getrandbits


class Battleships(QtGui.QMainWindow):
    def __init__(self):
        super(Battleships, self).__init__()
        self.initUI()

    def initUI(self):
        """
        loads ui from file
        sets images for several widgets
        """
        self.gameui = uic.loadUi("gameui.ui", self)  #load ui from file
        self.gameui.rotateleft.setIcon(QtGui.QIcon("rotateleft.png"))
        self.shipimage = QtGui.QPixmap("ship.png")
        self.gameui.imagelabel.setPixmap(self.shipimage)
        self.show()

        self.gameui.startbutton.clicked.connect(self.game)
        self.gameui.actionVerlaat_spel.triggered.connect(self.exitgame)

    def game(self):
        """
        assigns several important variables, connects buttons necessary for play.
        """
        
        self.boatlengths = [2,2,3,3,4]
        self.aiboats = [2,2,3,3,4]
        self.boatcoords = []
        self.playerrotation = True #orientation is True or False. True means vertical, False means horizontal
        self.aiships = self.generate()

        self.gameui.actionNieuwSpel.triggered.connect(self.restart)
        self.gameui.rotateleft.setEnabled(True)
        self.gameui.startbutton.setEnabled(False)
        self.gameui.rotateleft.clicked.connect(self.rotate)
        self.gameui.instructionlabel.setText("plaats schip #1, met lengte: 2")
        for row in range(1,10):
            for column in range(1,10):
                self.gameui.findChild(QtGui.QPushButton, "s" + str(row) + str(column)).clicked.connect(self.placeship)

    def placeship(self):
        """
        this function takes care of the player clicking what places they want their ships to be at.
        it takes the input, checks if their positions do not extend outside the board, or are the
        same as any other ships' positions.
        """

        if len(self.boatlengths) > 1:
            self.gameui.instructionlabel.setText("plaats schip #{}, met lengte: {}".format(5 - (len(self.boatlengths) - 2), self.boatlengths[1]))

        source = self.gameui.sender().objectName()
        row = int(source[1])
        column = int(source[2])
        
        
        shippositions = []
        for i in range(self.boatlengths[0]):
            if self.playerrotation: #is the ship aligned vertically?
                if row + self.boatlengths[0] < 11:
                    shippositions.append(str(row + i) + str(column))
            else:
                if column + self.boatlengths[0] < 11:
                    shippositions.append(str(row) + str(column + i))
        if shippositions != []:
            if not set(self.boatcoords).intersection(set(shippositions)):
            #empty sets return False, so if none of the elements of the shippositions list is in boatcoords we add the position of the ship to boatcoords
            #this is to avoid players placing two ships in the same location
                for pos in shippositions:
                    self.boatcoords.append(pos)
                self.boatlengths.remove(self.boatlengths[0])
                for ship in shippositions:
                    self.gameui.findChild(QtGui.QPushButton, "s" + str(ship[0]) + str(ship[1])).setEnabled(False)
                    self.gameui.findChild(QtGui.QPushButton, "s" + str(ship[0]) + str(ship[1])).setStyleSheet("background-color: blue")

        if self.boatlengths == []:
            self.prepareui()

    def prepareui(self):
        """
        sets up the ui for actually playing Battleships. connects the computer's grid, disconnects the player's.
        """
        self.gameui.instructionlabel.setText("klik op de coordinaten van de tegenstander om te schieten")
        self.gameui.rotateleft.setEnabled(False)
        for row in range(1,10):
            for column in range(1,10):
                self.gameui.findChild(QtGui.QPushButton, "s" + str(row) + str(column)).clicked.disconnect()
                self.gameui.findChild(QtGui.QPushButton, "c" + str(row) + str(column)).clicked.connect(self.shoot)


    def shoot(self):
        """
        self.shoot() is the function that handles the player clicking his target. it checks for orientation,
        then whether the shot is a valid coordinate.
        if so, it disables the button and makes it red.
        """
        source = self.gameui.sender().objectName()
        row = str(source[1])
        column = str(source[2])
        self.aishots = []

        for ship in self.aiships:
            clickedbutton = self.gameui.findChild(QtGui.QPushButton, "c" + row + column)
            if row == ship[0] and column == ship[1]:
                clickedbutton.setEnabled(False)
                clickedbutton.setStyleSheet("background-color: red")
                clickedbutton.setText(ship[2])
                self.aiships.remove(ship)
                self.gameui.instructionlabel.setText("je hebt raak geschoten")
                if self.aiships == []:
                    self.result(True)
            else:
                clickedbutton.setEnabled(False)
        self.aishoot()


    def aishoot(self):
        """
        self.aishoot() selects at random a coordinate to shoot at.
        after selecting 
        """
        shot = str(randrange(1,10)) + str(randrange(1,10))
        if shot not in self.aishots:
            self.aishots.append(shot)
            if shot in self.boatcoords:
                self.gameui.findChild(QtGui.QPushButton, "s" + shot[0] + shot[1]).setStyleSheet("background-color: red")
                self.boatcoords.remove(shot)
                self.gameui.instructionlabel.setText("de computer heeft raak geschoten")
        else:
            self.aishoot()

        if self.boatcoords == []:
            self.result(False)

    def result(self, WinOrLoseBool):
        """
        self.result(WinOrLoseBool) disables the board after a victory condition has been met and displays the result in the qt label.
        """
        for row in range(1,10):
            for column in range(1,10):
                cbutton = self.gameui.findChild(QtGui.QPushButton, "c" + str(row) + str(column))
                cbutton.clicked.disconnect()
                
        if WinOrLoseBool:
            self.gameui.instructionlabel.setText("je hebt gewonnen")
        else:
            self.gameui.instructionlabel.setText("je hebt verloren")
            
    def rotate(self):
        """
        self.rotate() inverts the self.playerrotation bool and changes the rotation image accordingly.
        """
        if self.playerrotation:
            self.playerrotation = False
            self.shipimage.swap(QtGui.QPixmap("ship1.png"))
            self.gameui.imagelabel.setPixmap(self.shipimage)
        else:
            self.playerrotation = True
            self.shipimage.swap(QtGui.QPixmap("ship.png"))
            self.gameui.imagelabel.setPixmap(self.shipimage)


    def generate(self):
        """
        self.generate() generates ai ships. this function returns a list of tuple containing x and y coordinates
        and their corresponding letter from a word at index [2]. functionally similar to placeships()
        """
        coordslist = []
        allpositions = []

        aiwords = self.choosewords()

        while self.aiboats != []: #loops until all ships have been placed
            row, column = randrange(1,10), randrange(1,10)
            orientation = bool(getrandbits(1)) #orientation is either True or False and chosen at random
            aiships = []
            currentpositions = []
           
            for i in range(self.aiboats[0]):
                if orientation and row + self.aiboats[0] < 10:
                    currentpositions.append(str(row + i) + str(column))
                elif not orientation and column + self.aiboats[0] < 10:
                    currentpositions.append(str(row) + str(column + i))

            if not set(allpositions).intersection(set(currentpositions)):
            #intersection() checks if any item from set 2 is in set 1. if that is not the case it returns False
                for i, position in enumerate(currentpositions):
                    allpositions.append(position)
                    aiships.append(position + aiwords[0][i])

            if aiships != []:
                for pos in aiships:
                    coordslist.append(pos)
                self.aiboats.remove(self.aiboats[0])
                aiwords.remove(aiwords[0])

        return coordslist

    def choosewords(self):
        """
        self.choosewords() returns list of words, ordered by length. sorting is necessary for the generate method,
        since it expects every word to be as long as the ship it's placing.
        sorting is more readable than a bunch of if statements.
        """
        lengte2 = []
        lengte3 = []
        lengte4 = []
        woordenlijst = []
        with open('woordenlijst.txt') as infile:
            for line in infile:
                if len(line) == 3:
                    lengte2.append(line[:-1])
                if len(line) == 4:
                    lengte3.append(line[:-1])
                if len(line) == 5:
                    lengte4.append(line[:-1])
            infile.close()

        for i in range(2):
            woordenlijst.append(lengte2[randrange(len(lengte2))])
            woordenlijst.append(lengte3[randrange(len(lengte3))])
        woordenlijst.append(lengte4[randrange(len(lengte4))])
        woordenlijst.sort(key=len)

        return woordenlijst

    def restart(self):
        """
        self.restart() resets all widgets to their original state and calls on self.game() to restart the game.
        """

        for row in range(1,10):
            for column in range(1,10):
                cbutton = self.gameui.findChild(QtGui.QPushButton, "c" + str(row) + str(column))
                sbutton = self.gameui.findChild(QtGui.QPushButton, "s" + str(row) + str(column))
                
                sbutton.setEnabled(True)
                sbutton.setStyleSheet("background-color: None")
                cbutton.setEnabled(True)
                cbutton.setStyleSheet("background-color: None")
                cbutton.setText("")

        self.game()
                
    def exitgame(self):
        sys.exit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Battleships()
    sys.exit(app.exec_())
