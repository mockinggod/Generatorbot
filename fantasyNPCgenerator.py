import random
import randomnamegenerator
import names
import numpy as np
import homebrew as hb

#The output is an object with seven keys output["name"], output["age"], output["characteristic"], output["trait"], output["occupation"], output["gender"], output["secret"]

fantasyocupationstype = ["Academia", "Artisan", "Bourgeoisie", "Common", "Law", "Magic", "Nature", "Outlaw", "Performer", "Religion", "Warrior"]
 
with open("NPCcharacteristics.txt", encoding='latin-1') as f:
    characteristiclist = f.read().splitlines() 
	
with open("medievalNPCcharacteristics.txt", encoding='latin-1') as f:
    characteristiclist += f.read().splitlines() 
	
with open("NPCtraits.txt", encoding='latin-1') as f:
    traitlist = f.read().splitlines() 	
	

occupationlist = (hb.arrayreader("medievalNPCoccupation.txt"))
occupationlist += (hb.arrayreader("fantasyNPCoccupation.txt"))	
occupationlist = hb.rotate(occupationlist)
	
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
	
def main(races=[], ethnicity = 'eng', occupation = None, occupations = [1,1,1,1,1,1,1,1,1,1,1]):
# Generates a random Non Player Character from tables and RNGs, the output is an object
	
	NPC = {} 
	
	NPC["name"] = ""
	
	if races==[]:
	
		NPC["race"] = ""
		
		rand = random.random()
		
		if ethnicity in names.humangentypelist:
			gen = True
		else:
			gen = False
	
		if rand < 0.496:
			NPC["gender"] = "male"
			string = ethnicity + "m"
			NPC["name"] = names.name(gen, string) + ' '
		elif rand < 0.978:
			NPC["gender"] = "female"
			string = ethnicity + "f"
			NPC["name"] = names.name(gen, string) + ' '
		else:
			NPC["gender"] = ""
			string = ethnicity + "m"
			NPC["name"] = names.name(gen, string) + ' '
	
		if random.random() < 0.5:
			if ethnicity in names.nosurnamelist:
				string = ethnicity + "m"
				NPC["name"] += names.name(True, string)
			else:
				string = ethnicity + "sur"
				NPC["name"] += names.name(gen, string)
				
		raceocupations = [1,1,1,1,1,1,1,1,1,1,1]
		
	else:
		sumw = 0.0
		for race in races:
			sumw += float(race['weight'])
			
		rand = random.random()*sumw
		dum = 0
		for race in races:
			dum += float(race['weight'])
			if rand < dum:
				NPC["race"] = race['racename']
				NPC["gender"] = race['gender'] 
				gen = race["names"] in names.humangentypelist
				NPC["name"] = names.name(gen, race["names"]) 
				raceocupations = race['occupations']
				if race["surnames"] != "none" and random.random() <0.5:
					gen = race["surnames"] in names.humangentypelist
					NPC["name"] += ' ' + names.name(gen, race["surnames"]) 
				
				break
			
			

	NPC["age"] = random.choice([" young", " ", "n older", "n elder"])
	NPC["characteristic"] = str(random.choice(characteristiclist))
	NPC["trait"] = random.choice(traitlist)
	
	if occupation == None:
		occupations = [float(occupations[i])*float(raceocupations[i]) for i in range(11)]		
		
		occupationweightlist = []
		
		for i in range(len(occupationlist[2])):
			occupationlist[3][i] = float(occupationlist[3][i])
			
			for j in range(11):
				
				if occupationlist[2][i] == fantasyocupationstype[j]:
									
					occupationweightlist.append(occupationlist[3][i]*occupations[j])
					
					
		index = np.random.choice(range(len(occupationlist[0])), p=hb.normalise(occupationweightlist))
		
		if NPC["gender"] == "female":
			NPC["occupation"] = occupationlist[1][index]
		else:
			NPC["occupation"] = occupationlist[0][index]
		
		NPC["occupationgenerated"] = True 
		
		
		if occupationlist[0][index] == occupationlist[1][index]:
			NPC["occupationgendered"] = False
		else:
			NPC["occupationgendered"] = True 
	else:
		NPC["occupation"] = occupation
		NPC["occupationgenerated"] = False 
		NPC["occupationgendered"] = False
		
	
	if random.random() < 0.40:
		NPC["secret"] = np.random.choice(secretlist)
	else:
		NPC["secret"] = "Has no secret"
		
	return(NPC)
