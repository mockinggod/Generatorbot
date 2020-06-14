import random
import randomnamegenerator

#The output is an object with seven keys output["name"], output["age"], output["characteristic"], output["trait"], output["occupation"], output["gender"], output["secret"]
 
with open("NPCcharacteristics.txt", encoding='latin-1') as f:
    characteristiclist = f.read().splitlines() 
	
with open("medievalNPCcharacteristics.txt", encoding='latin-1') as f:
    characteristiclist += f.read().splitlines() 
	
with open("NPCtraits.txt", encoding='latin-1') as f:
    traitlist = f.read().splitlines() 	
	
with open("fantasyNPCoccupation.txt", encoding='latin-1') as f:
    occupationlist = f.read().splitlines() 	
	
with open("medievalNPCoccupation.txt", encoding='latin-1') as f:
    occupationlist += f.read().splitlines() 	
	
with open("NPCsecrets.txt", encoding='latin-1') as f:
    secretlist = f.read().splitlines() 	
	
with open("fantasyNPCsecrets.txt", encoding='latin-1') as f:
    secretlist += f.read().splitlines() 	
	
with open("medievalNPCsecrets.txt", encoding='latin-1') as f:
    secretlist += f.read().splitlines() 
	
with open("femalename.txt", encoding='latin-1') as f:
    femalenamelist = f.read().splitlines()
	
with open("medievalfemalename.txt", encoding='latin-1') as f:
    femalenamelist += f.read().splitlines() 
	
with open("malename.txt", encoding='latin-1') as f:
    malenamelist = f.read().splitlines() 	
	
with open("medievalmalename.txt", encoding='latin-1') as f:
    malenamelist += f.read().splitlines() 
	
with open("surname.txt", encoding='latin-1') as f:
    surnamelist = f.read().splitlines() 	
	
with open("medievalsurname.txt", encoding='latin-1') as f:
    surnamelist += f.read().splitlines() 
	
def main(occupation = "generate"):
# Generates a random Non Player Character from tables and RNGs, the output is an object

	NPClist = []

	i = len(NPClist)
	
	NPClist.append({})
	

	if random.random() < 0.496:
		NPClist[i]["gender"] = "male"
		NPClist[i]["name"] = random.choice(malenamelist)
	else:
		if random.random() < 0.978:
			NPClist[i]["gender"] = "female"
			NPClist[i]["name"] = random.choice(femalenamelist)
		else:
			NPClist[i]["gender"] = "androgynous"
			NPClist[i]["name"] = random.choice([random.choice(malenamelist),random.choice(femalenamelist)])
			
	if random.random() < 0.5:
		NPClist[i]["name"] += " " + random.choice(surnamelist)
	
	
	NPClist[i]["age"] = random.choice(["young adult", "adult", "older adult", "elder"])		
	NPClist[i]["characteristic"] = str(random.choice(characteristiclist))
	NPClist[i]["trait"] = random.choice(traitlist)
	
	if occupation == "generate":
		NPClist[i]["occupation"] = random.choice(occupationlist)
		NPClist[i]["occupationgenerated"] = True 
	else:
		NPClist[i]["occupation"] = occupation
		NPClist[i]["occupationgenerated"] = False 
	
	if random.random() < 0.40:
		NPClist[i]["secret"] = random.choice(secretlist)
	else:
		NPClist[i]["secret"] = "Has no secret"
		
	return(NPClist[i])
