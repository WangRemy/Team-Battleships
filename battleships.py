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

        self.gameui.rotateleft.setEnabled(True)
        self.gameui.rotateright.setEnabled(True)
        self.gameui.startbutton.setEnabled(False)

        #self.gameui.rotateleft.clicked.connect()
        #self.gameui.rotateright.clicked.connect()

        self.aiships = self.generate()

    def generate(self):
        """
        generates ai ships. this function returns a list of tuples containing x and y coordinates, and their corresponding letter from a word.
        """
        coordslist = []

        boats = self.boatlengths
        aiwords = self.choosewords()

        while boats != []: #reversed zodat de for loop doorgaat ook al worden er elementen verwijderd
            basisx, basisy = randrange(1,9), randrange(1,9)            
            orientation = bool(getrandbits(1)) #orientation is True or False. True means vertical, False means horizontal

            if orientation == True: #als schip verticaal geörienteerd is
                if basisx + boats[0] <10:
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
        
        return woordenlijst



    def exitgame(self):
        sys.exit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Battleships()
    sys.exit(app.exec_())



