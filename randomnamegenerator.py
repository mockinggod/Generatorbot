import random

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z", "w"]
vowels = ["a", "e", "i", "o", "u", "y"]


def main():
	letternum = random.triangular(2,6,10)
	name = ""
	
	if random.random() > 0.5:
		name = name + random.choice(consonants)
		c = 1
	else:
		name = name + random.choice(vowels)
		c = 0
		
	while len(name) < letternum:
	
		if c == 1: 
			if random.random() > 0.98:
				name = name + random.choice(consonants)
				c = 1
			else:
				name = name + random.choice(vowels)
				c = 0
				
		if c == 0: 
			if random.random() < 0.98:
				name = name + random.choice(consonants)
				c = 1
			else:
				name = name + random.choice(vowels)
				c = 0
	
	return(name.capitalize())