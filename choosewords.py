from random import randrange

def choosewords():
	woordenlijst = []
	for i in range(2):
		with open("len2.txt") as f:
			woord = f.readline(randrange(sum(1 for line in f)))
			woordenlijst.append(woord[:-1])
		with open("len3.txt") as f:
			woord = f.readline(randrange(sum(1 for line in f)))
			woordenlijst.append(woord[:-1])
	with open("len4.txt") as f:
			woord = f.readline(randrange(sum(1 for line in f)))
			woordenlijst.append(woord[:-1])
	f.close()
	return woordenlijst
