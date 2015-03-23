#!/usr/bin/python

from PyQt4 import QtCore, QtGui, uic
import sys

woordlen2 = ['ad', 'af', 'ah', 'al', 'as', 'at', 'au', 'be', 'by', 'cd', 'cm', 'co', 'de', 'do', 'ei', 'el', 'en', 'er', 'es', 'ex', 'ga', 'ge', 'go', 'ha', 'he', 'hé', 'ie', 'ij', 'ik', 'in', 'is', 'ja', 'je', 'ka', 'kg', 'la', 'ma', 'me', 'na', 'nu', 'of', 'oh', 'ok', 'om', 'on', 'op', 'or', 'pa', 'pi', 're', 'se', 'te', 'to', 'tv', 'uk', 'up', 'ut', 'uw', 'we', 'ze', 'zo']
woordlen3 = ['aan', 'abc', 'ach', 'ade', 'air', 'all', 'als', 'alt', 'and', 'are', 'arm', 'art', 'ave', 'avn', 'bad', 'bah', 'bak', 'bal', 'bed', 'bef', 'bel', 'ben', 'bes', 'bie', 'big', 'bij', 'bit', 'bob', 'bod', 'bol', 'bor', 'bos', 'bot', 'bou', 'box', 'boy', 'bus', 'can', 'cel', 'com', 'dag', 'dak', 'dan', 'dat', 'del', 'den', 'der', 'des', 'dia', 'die', 'dik', 'dit', 'doe', 'dol', 'dom', 'don', 'dug', 'dun', 'duo', 'dus', 'duw', 'eau', 'eed', 'een', 'eer', 'eis', 'elf', 'elk', 'els', 'end', 'ene', 'era', 'ere', 'erg', 'ers', 'fan', 'fax', 'fel', 'fin', 'gaf', 'gap', 'gas', 'gat', 'gek', 'gel', 'gha', 'gif', 'gis', 'god', 'gun', 'had', 'hap', 'heb', 'hei', 'hel', 'hem', 'hen', 'her', 'het', 'hij', 'hik', 'hip', 'hoc', 'hoe', 'hol', 'hou', 'hul', 'hun', 'ijs', 'jam', 'jan', 'jas', 'jij', 'jip', 'jli', 'jou', 'kan', 'kar', 'kat', 'ken', 'kin', 'kip', 'koe', 'kok', 'kom', 'kon', 'kop', 'kun', 'kus', 'kut', 'lab', 'laf', 'lag', 'lam', 'las', 'lat', 'lay', 'lef', 'leg', 'lek', 'les', 'let', 'lid', 'lig', 'lof', 'los', 'lot', 'lui', 'lul', 'mag', 'mak', 'man', 'map', 'mar', 'mee', 'mei', 'men', 'mes', 'met', 'mij', 'min', 'mis', 'moe', 'mom', 'mop', 'mot', 'nam', 'nee', 'nek', 'nes', 'net', 'nog', 'non', 'not', 'nou', 'nut', 'ode', 'off', 'ons', 'oog', 'ook', 'oor', 'opa', 'oud', 'out', 'pad', 'pak', 'pan', 'pap', 'par', 'pas', 'pen', 'per', 'pet', 'pij', 'pol', 'pot', 'pro', 'qua', 'red', 'rel', 'rem', 'reu', 'rij', 'rla', 'rob', 'rok', 'rol', 'rom', 'rop', 'rot', 'rpi', 'rug', 'ruk', 'sap', 'sar', 'sec', 'set', 'sew', 'sex', 'sis', 'slo', 'sol', 'som', 'spa', 'sta', 'sto', 'sub', 'suu', 'tab', 'tal', 'tbr', 'tel', 'tem', 'ten', 'ter', 'tik', 'tip', 'tja', 'toe', 'tof', 'tol', 'ton', 'top', 'tot', 'tri', 'try', 'typ', 'uil', 'uit', 'ups', 'uur', 'vak', 'val', 'van', 'var', 'vat', 'vel', 'ver', 'vet', 'via', 'vil', 'vip', 'vol', 'vos', 'vul', 'vvd', 'wal', 'war', 'was', 'wat', 'web', 'wee', 'weg', 'wei', 'wel', 'wet', 'wie', 'wij', 'wil', 'win', 'wit', 'won', 'wou', 'zag', 'zak', 'zal', 'zat', 'zee', 'zeg', 'zei', 'zen', 'zes', 'zet', 'zie', 'zij', 'zin', 'zit', 'zou', 'zul', 'zus']
woordlen4 = ['aard', 'aars', 'acht', 'adam', 'adel', 'adem', 'alfa', 'alle', 'alom', 'ambt', 'anna', 'anno', 'anti', 'apen', 'area', 'auto', 'baal', 'baan', 'baas', 'baby', 'back', 'balk', 'band', 'bang', 'bank', 'bars', 'beat', 'been', 'beet', 'bent', 'berg', 'best', 'bied', 'bier', 'bijt', 'blad', 'blij', 'blik', 'blok', 'body', 'boek', 'boel', 'boem', 'boer', 'bond', 'bons', 'bood', 'boog', 'boom', 'boos', 'boot', 'bord', 'bouw', 'boze', 'brak', 'brei', 'brok', 'bron', 'brug', 'brui', 'bugs', 'buik', 'bulk', 'care', 'case', 'cast', 'cent', 'chef', 'club', 'coca', 'code', 'cola', 'coma', 'coup', 'daar', 'dame', 'dank', 'dans', 'darm', 'data', 'date', 'deed', 'deel', 'dele', 'deur', 'deze', 'dief', 'diep', 'dijk', 'ding', 'dirk', 'dito', 'doek', 'doel', 'doem', 'doen', 'doet', 'dood', 'dook', 'door', 'doos', 'dorp', 'down', 'drie', 'drop', 'druk', 'duel', 'duin', 'dure', 'durf', 'duur', 'echt', 'edam', 'eend', 'eens', 'eeuw', 'eind', 'eist', 'elan', 'elke', 'enge', 'enig', 'eraf', 'eren', 'erge', 'erin', 'erom', 'erop', 'eten', 'euro', 'even', 'faam', 'face', 'fans', 'fase', 'feit', 'fijn', 'film', 'fles', 'font', 'fors', 'foto', 'fout', 'fris', 'gaan', 'gaap', 'gade', 'gang', 'gard', 'gauw', 'geef', 'geel', 'geen', 'geil', 'geld', 'gele', 'gene', 'gent', 'geur', 'giet', 'giga', 'ging', 'gips', 'giro', 'glas', 'goed', 'golf', 'goor', 'goud', 'gouw', 'graf', 'gram', 'gras', 'grof', 'haak', 'haal', 'haar', 'haat', 'half', 'hand', 'hang', 'hans', 'hard', 'hart', 'hebt', 'heel', 'heen', 'heer', 'heet', 'heil', 'hein', 'hele', 'help', 'hemd', 'heup', 'heus', 'hief', 'hier', 'high', 'hing', 'hoed', 'hoef', 'hoek', 'hoge', 'home', 'hond', 'hoog', 'hoop', 'hoor', 'houd', 'huid', 'huis', 'hulp', 'hype', 'idee', 'iets', 'info', 'iris', 'jaap', 'jaar', 'java', 'jong', 'jouw', 'juli', 'juni', 'kaan', 'kaft', 'kaki', 'kale', 'kalm', 'kamp', 'kans', 'kant', 'kast', 'keek', 'keel', 'keer', 'kees', 'keil', 'kent', 'kerk', 'kern', 'kiel', 'kies', 'kijk', 'kiki', 'kind', 'klap', 'klas', 'klem', 'klik', 'knap', 'knel', 'knip', 'knop', 'koek', 'komt', 'kont', 'koor', 'koos', 'kort', 'kost', 'koud', 'krol', 'kunt', 'kurk', 'kuub', 'kuur', 'kwam', 'kwik', 'laag', 'laat', 'lach', 'lady', 'lage', 'lama', 'land', 'lang', 'lans', 'last', 'leed', 'leeg', 'leek', 'leer', 'lees', 'lege', 'legt', 'leid', 'leuk', 'leve', 'lief', 'liep', 'lier', 'lies', 'liet', 'lift', 'ligt', 'lijf', 'lijn', 'link', 'list', 'live', 'loco', 'logo', 'lokt', 'long', 'look', 'loop', 'lord', 'luid', 'lukt', 'lust', 'luxe', 'maag', 'maak', 'maal', 'maan', 'maar', 'maas', 'maat', 'made', 'mail', 'main', 'mama', 'mams', 'mand', 'mark', 'mars', 'mate', 'mede', 'meen', 'meer', 'meet', 'meid', 'melk', 'mens', 'menu', 'mest', 'miet', 'mijd', 'mijn', 'mikt', 'mild', 'mime', 'mist', 'mits', 'mode', 'moed', 'moet', 'molk', 'mond', 'mooi', 'more', 'most', 'muil', 'muis', 'munt', 'must', 'muur', 'naam', 'naar', 'name', 'nare', 'nasi', 'nauw', 'neef', 'neem', 'neer', 'nerf', 'nest', 'neus', 'niet', 'niks', 'noch', 'noem', 'none', 'noot', 'norm', 'nota', 'ogen', 'olie', 'onze', 'oogt', 'ooit', 'oost', 'open', 'orde', 'oren', 'oude', 'outs', 'ouwe', 'over', 'paal', 'paar', 'pakt', 'palm', 'papa', 'paps', 'park', 'past', 'paus', 'pech', 'pers', 'pest', 'piek', 'piet', 'pijn', 'pijp', 'plan', 'plas', 'plat', 'plek', 'plus', 'pond', 'pool', 'poot', 'post', 'pret', 'prof', 'prop', 'pulp', 'punt', 'puur', 'raad', 'raam', 'raar', 'rade', 'rake', 'ramp', 'rand', 'rare', 'rato', 'rauw', 'rede', 'redt', 'reed', 'rein', 'reis', 'rest', 'riep', 'rijk', 'rijn', 'rijp', 'rock', 'rode', 'roem', 'roep', 'roes', 'roll', 'rond', 'rood', 'rook', 'room', 'roos', 'rouw', 'roze', 'ruim', 'ruit', 'rust', 'ruwe', 'saai', 'sari', 'sein', 'seks', 'semi', 'shit', 'show', 'site', 'slag', 'slap', 'slim', 'slop', 'slot', 'smid', 'smit', 'snee', 'snel', 'snik', 'snit', 'snor', 'soap', 'soep', 'sofa', 'soms', 'span', 'spel', 'spot', 'spul', 'stad', 'staf', 'stak', 'stam', 'stap', 'star', 'stek', 'stel', 'stem', 'stik', 'stil', 'stof', 'stop', 'stro', 'stuk', 'taak', 'taal', 'talk', 'tang', 'tart', 'taxi', 'team', 'telt', 'tent', 'term', 'tien', 'tijd', 'tilt', 'time', 'tips', 'toch', 'toen', 'tong', 'toon', 'tour', 'touw', 'tram', 'trap', 'trek', 'trip', 'trof', 'trok', 'trom', 'trui', 'tuin', 'turk', 'twee', 'type', 'unie', 'uren', 'uurs', 'uwer', 'vaag', 'vaak', 'vage', 'vals', 'valt', 'vast', 'veel', 'veen', 'veer', 'veld', 'vele', 'verf', 'vice', 'viel', 'vier', 'vies', 'vijf', 'vind', 'ving', 'vive', 'vlak', 'vlam', 'vlek', 'vlug', 'voel', 'voer', 'voet', 'volk', 'volt', 'vond', 'voor', 'voos', 'vorm', 'vree', 'vrij', 'vuig', 'vuil', 'vult', 'vuur', 'waak', 'waal', 'waan', 'waar', 'waas', 'wang', 'want', 'ware', 'warm', 'watt', 'wauw', 'week', 'weer', 'wees', 'weet', 'weke', 'wekt', 'welk', 'wens', 'werd', 'werf', 'werk', 'west', 'wiel', 'wier', 'wiet', 'wijd', 'wijk', 'wijn', 'wijs', 'wild', 'wilt', 'wind', 'wint', 'wist', 'wolf', 'wolk', 'wond', 'woon', 'word', 'worp', 'wurm', 'zaak', 'zaal', 'zake', 'zakt', 'zand', 'zeef', 'zeer', 'zege', 'zegt', 'zelf', 'zere', 'zich', 'ziek', 'ziel', 'zien', 'ziet', 'zijn', 'zoek', 'zong', 'zoog', 'zoom', 'zoon', 'zorg', 'zuid', 'zult', 'zwak', 'zwom']

class Battleships(QtGui.QMainWindow):
	def __init__(self):
		super(Battleships, self).__init__()
		self.gameui = uic.loadUi('gameui.ui', self)  #load ui from file
		self.game_started = False
		self.drawgrid()
		self.show()
	
	def drawgrid(self):
		spelerWidget = self.gameui.spelerWidget
		computerWidget = self.gameui.computerWidget
		
		self.spelerWidget.setRowCount(10)
		self.computerWidget.setRowCount(10)
		self.spelerWidget.setColumnCount(10)
		self.computerWidget.setColumnCount(10)
		
		for i in range(10):
			self.spelerWidget.setColumnWidth(i,34)
			self.computerWidget.setColumnWidth(i,34)
			
	def exit(self):
		sys.exit()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	w = Battleships()
	sys.exit(app.exec_())



