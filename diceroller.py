import numpy as np

def formatsum(user, dice, mod):

	result = sum(dice) + mod

	if mod<0:
		return(user + "'s roll \n" + str(dice) + "  " + str(mod) + "\nResult: " + str(result))
	else:
		return(user + "'s roll \n" + str(dice) + "  +" + str(mod) + "\nResult: " + str(result))		

def whbt():
# Stands for weird home brew thing
	dice = []
	dice.append(np.random.randint(1, 9))
	if dice[0] == 1:
		dice.extend(explo(8))
		newdice = []
		newdice.append(dice[0])
		for die in dice[1:]:
			newdice.append(-1*die)
		dice = newdice

	elif dice[0] == 8:
		dice.extend(explo(8))
		
	return(dice)

	
def explo(faces, triger = True):
	if triger:
		triger = faces
	dice = []
	dice.append(np.random.randint(1,faces+1))
	while dice[-1] >= triger:
		dice.append(np.random.randint(1,faces+1))
		
	return(dice)