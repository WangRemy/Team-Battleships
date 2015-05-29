#!/usr/bin/python

from PyQt4 import QtCore, QtGui, uic
import sys
from random import randrange, getrandbits


class Battleships(QtGui.QMainWindow):
    def __init__(self):
        super(Battleships, self).__init__()
        self.gameui = uic.loadUi('gameui.ui', self)  #load ui from file
        self.show()

        self.gameui.startbutton.clicked.connect(self.game)
        self.gameui.actionVerlaat_spel.triggered.connect(self.exitgame)

    def game(self):
        self.boatlengths = [2,2,3,3,4]
        self.boatcoords = [] 

        self.gameui.rotateleft.setEnabled(True)
        self.gameui.startbutton.setEnabled(False)

        #self.gameui.rotateleft.clicked.connect()
        #self.gameui.rotateright.clicked.connect()

        self.aiships = self.generate()

        for row in range(1,9):
            for column in range(1,9):
                self.coord = self.gameui.findChild(QtGui.QPushButton, "s" + str(row) + str(column))
                self.coord.clicked.connect(self.placeship)

    def placeship(self):
        source = self.gameui.sender().objectName()
        row = int(source[1])
        column = int(source[2])

        #check if coords are valid
        if self.boatlengths != []:
            if row + self.boatlengths[0] < 10:
                shippositions = []
                for i in range(self.boatlengths[0]):
                    shippositions.append(str(row) + str(column))
                if not set(self.boatcoords).intersection(set(shippositions)):
                #empty sets return False, so if none of the elements of the shippositions list is in boatcoords we add the position of the ship to boatcoords
                    for pos in shippositions:
                        self.boatcoords.append(pos)
                    self.boatlengths.remove(self.boatlengths[0])
                    self.gameui.findChild(QtGui.QPushButton, source).setEnabled(False)
                    self.gameui.findChild(QtGui.QPushButton, source).setStyleSheet("background-color: red")
        else:
            self.startgame()

    def startgame(self):
        print("hoi")
        

    def generate(self):
        """
        generates ai ships. this function returns a list of tuples containing x and y coordinates, and their corresponding letter from a word.
        """
        coordslist = []

        boats = [2,2,3,3,4]
        aiwords = self.choosewords()

        while boats != []:
            basisx, basisy = randrange(1,9), randrange(1,9)            
            orientation = bool(getrandbits(1)) #orientation is True or False. True means vertical, False means horizontal

            if orientation: #als schip verticaal geörienteerd is
                if basisx + boats[0] < 10: #steekt het schip niet buiten het bord uit?
                    for i in range(boats[0]):
                        coordslist.append((basisx + i, basisy, aiwords[0][i]))
                    boats.remove(boats[0])
                    aiwords.remove(aiwords[0])
            else:
                if basisy + boats[0] < 10:
                    for i in range(boats[0]):
                        coordslist.append((basisx, basisy + i, aiwords[0][i]))
                    boats.remove(boats[0])
                    aiwords.remove(aiwords[0])        
        return coordslist


    def choosewords(self):
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



    def exitgame(self):
        sys.exit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Battleships()
    sys.exit(app.exec_())
