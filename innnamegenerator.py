import numpy as np

# Generates a genuine sounding inn name from two tables

with open("innnamespart1.txt") as f:
    part1 = f.read().splitlines() 	
	
with open("innnamespart2.txt") as f:
    part2 = f.read().splitlines() 	
	
def main():
# Generates a inn name from two components 

	if np.random.random() < 0.1:
	
		output = "The " + np.random.choice(part2)
		
	else:

		output = "The " + np.random.choice(part1) + " " + np.random.choice(part2)
		
	if np.random.random() < 0.05:
	
		output += " Inn"
	
	return(output)