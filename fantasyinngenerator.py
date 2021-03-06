import numpy as np
import innnamegenerator as name
import homebrew as hb

odditylist = (hb.arrayreader("innoddity.txt"))
odditylist += (hb.arrayreader("fantasyinnoddity.txt"))
odditylist = (hb.rotate(odditylist))

with open("innspeciality.txt") as f:
    specialtylist = f.read().splitlines() 	
	
with open("innsecret.txt") as f:
    secretlist = f.read().splitlines() 
with open("fantasyinnsecret.txt") as f:
    secretlist += f.read().splitlines() 

def main():
	output = {}
	
	output["name"] = name.main()
	output["oddity"] = np.random.choice(odditylist[0])
	output["specialty"] = np.random.choice(specialtylist)
	if np.random.random() < 0.80:
		output["secret"] = "The beer is watered down"
	else:
		output["secret"] = np.random.choice(secretlist)
	
	return(output)