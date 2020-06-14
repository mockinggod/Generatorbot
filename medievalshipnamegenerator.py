import numpy as np

# Generates a genuine sounding ship name from two tables

with open("shipnames.txt") as f:
    shipnames = f.read().splitlines() 

with open("shipnames.txt") as f:
    shipnames = f.read().splitlines() 

with open("shipnamespt1.txt") as f:
    part1 = f.read().splitlines() 	
	
with open("shipnamespt2.txt") as f:
    part2 = f.read().splitlines() 	
	
with open("malename.txt", encoding='latin-1') as f:
    name = f.read().splitlines() 
	
with open("femalename.txt", encoding='latin-1') as f:
    name += f.read().splitlines() 
	
with open("medievalmalename.txt", encoding='latin-1') as f:
    name += f.read().splitlines() 
	
with open("medievalfemalename.txt", encoding='latin-1') as f:
    name += f.read().splitlines() 
	
with open("surname.txt", encoding='latin-1') as f:
    name += f.read().splitlines() 
	
with open("medievalsurname.txt", encoding='latin-1') as f:
    name += f.read().splitlines() 
	
def main():
# Generates a inn name from two components 

	rand = np.random.random()

	if rand < 0.1:
	
		output = np.random.choice(shipnames)
		
	elif rand < 0.3:
		
		output = "The " + np.random.choice(part2)
	
	elif rand < 0.4:
	
		output = "The " + np.random.choice(part1)
	
	elif rand < 0.45:
	
		output = "@name@'s " + np.random.choice(part2)
	
	else:

		output = "The " + np.random.choice(part1) + " " + np.random.choice(part2)
		
	output = output.replace("@name@", str(np.random.choice(name)), 1)
		
	
	return(output)