from random import randrange

def generate(shiplengths):
	#defines coordinates for computer battleships
	coords = {}
	
	#iterates each ship in list
	for length in shiplengths:
		y = []
		x = []
		
		x.append(randrange(1,10))
		y.append(randrange(1,10))
		orientation = randrange(1,4)
		if orientation == 1: #schip naar noorden gericht
			for i in range(length - 1):
				x.append(x[0] + i + 1)
		elif orientation == 2:#naar zuiden
			for i in range(length - 1):
				x.append(x[0] - i - 1)
		elif orientation == 3:#naar oosten
			for i in range(length - 1):
				y.append(y[0] + i + 1)
		else:#naar westen
			for i in range(length - 1):
				y.append(y[0] - i - 1)
				
		#appends the coordinates of each ship to the coords dict
		coords[tuple(x)] = tuple(y)
		
	return coords
		
