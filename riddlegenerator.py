import numpy as np
import homebrew as hb

riddlelist = (hb.arrayreader("riddles.txt"))
# List of all riddles, needs to be rotated to be human readable.


def main(input):
	input = int(input)
	if(input==0):
	#leveledlist is the list of riddles that fit the difficulty parameter 
		leveledlist = riddlelist
	else:
		leveledlist = []
		for riddle in riddlelist:
			if(int(riddle[0]) == input):
				leveledlist.append(riddle)
				leveledlist.append(riddle) 
				leveledlist.append(riddle)
			if(abs(int(riddle[0]) - input) == 0):
				leveledlist.append(riddle)
				#Riddles with difficulties +- 1  the stated value can be picked but they are a 1/3 as likely. 
				
	leveledlist = (hb.rotate(leveledlist))
	output = {}
	i = np.random.randint(0, len(leveledlist[0]))
	output["riddle"] = leveledlist[1][i]
	output["answer"] = leveledlist[2][i]
	
	return(output)
