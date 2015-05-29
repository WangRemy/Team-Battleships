#!/usr/bin/python

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
        self.boatlengths = [2,2,3,3,4]
        self.boatcoords = []
        self.playerrotation = True #orientation is True or False. True means vertical, False means horizontal

        self.gameui.rotateleft.setEnabled(True)
        self.gameui.startbutton.setEnabled(False)

        self.gameui.rotateleft.clicked.connect(self.rotate)

        self.aiships = self.generate()

        for row in range(1,10):
            for column in range(1,10):
                self.gameui.findChild(QtGui.QPushButton, "s" + str(row) + str(column)).clicked.connect(self.placeship)

    def placeship(self):
        """
        this function takes care of the player clicking what places they want their ships to be at.
        it takes the input, checks if their positions do not extend outside the board, or are the
        same as any other ships' positions.
        """
        source = self.gameui.sender().objectName()
        row = int(source[1])
        column = int(source[2])

        if self.playerrotation: #is the ship aligned vertically?
            if row + self.boatlengths[0] < 11:
                shippositions = []
                for i in range(self.boatlengths[0]):
                    shippositions.append(str(row + i) + str(column))
                if not set(self.boatcoords).intersection(set(shippositions)):
                #empty sets return False, so if none of the elements of the shippositions list is in boatcoords we add the position of the ship to boatcoords
                #this is to avoid players placing two ships in the same location
                    for pos in shippositions:
                        self.boatcoords.append(pos)
                    self.boatlengths.remove(self.boatlengths[0])
                    for ship in shippositions:
                        self.gameui.findChild(QtGui.QPushButton, "s" + str(ship[0]) + str(ship[1])).setEnabled(False)
                        self.gameui.findChild(QtGui.QPushButton, "s" + str(ship[0]) + str(ship[1])).setStyleSheet("background-color: blue")

        else:
            if column + self.boatlengths[0] < 11:
                shippositions = []
                for i in range(self.boatlengths[0]):
                    shippositions.append(str(row) + str(column + i))
                if not set(self.boatcoords).intersection(set(shippositions)):
                    for pos in shippositions:
                        self.boatcoords.append(pos)
                    self.boatlengths.remove(self.boatlengths[0])
                    for ship in shippositions:
                        self.gameui.findChild(QtGui.QPushButton, "s" + str(ship[0]) + str(ship[1])).setEnabled(False)
                        self.gameui.findChild(QtGui.QPushButton, "s" + str(ship[0]) + str(ship[1])).setStyleSheet("background-color: blue")

        if self.boatlengths == []:
            self.preparenpc()

    def preparenpc(self):
        for row in range(10):
            for column in range(10):
                self.gameui.findChild(QtGui.QPushButton, "s" + str(row) + str(column)).disconnect()
                self.gameui.findChild(QtGui.QPushButton, "s" + str(row) + str(column)).clicked.connect(self.shoot)

    def shoot(self):
        source = self.gameui.sender().objectName()
        row = int(source[1])
        column = int(source[2])

        

        self.aiships

    def rotate(self):
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
        generates ai ships. this function returns a list of strings containing x and y coordinates at indexes
        [0] and [1], and their corresponding letter from a word at index [2].
        """
        coordslist = []

        boats = [2,2,3,3,4]
        aiwords = self.choosewords()

        while boats != []:
            basisx, basisy = randrange(1,9), randrange(1,9)
            orientation = bool(getrandbits(1))

            if orientation: #als schip verticaal geörienteerd is
                if basisx + boats[0] < 10: #steekt het schip niet buiten het bord uit?
                    for i in range(boats[0]):
                        coordslist.append(str(basisx + i) + str(basisy) + aiwords[0][i])
                    boats.remove(boats[0])
                    aiwords.remove(aiwords[0])
            else:
                if basisy + boats[0] < 10:
                    for i in range(boats[0]):
                        coordslist.append(str(basisx) + str(basisy + i) + aiwords[0][i])
                    boats.remove(boats[0])
                    aiwords.remove(aiwords[0])
        print(coordslist)
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
