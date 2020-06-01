import random
import fantasyinngenerator

adjectivelist = ["A grim", "A spotless", "An overcrowded", "A worn down", "An ancient", "A brand new", "A creepy", "A rough", "A fancy",\
	"An ugly", "A noisy", "A elegant", "A fashionable", "A high end", "A sprawling"]


institutionlist = ["inn", "tavern", "trading post", "temple", "library", "university", "park"]
	
tradingnameslist = ["Trading Post", "Bazaar", "Market", "Arcade", "Souk"]

templenameslist = ["Church", "Temple", "Chapel", "Cathedral"]
templeadjectivelist = ["Holy", "Blessed", "Savior", "Revered", "Sacred", "Hallowed"]
succourlist = ["Orphanage", "Healing", "Protection", "Feeding", "Caritative Care", "Housing"]

directionslist = ["North", "South", "East", "West", "Old", "New", "Morning", "Evening"]

parknameslist = ["Park", "Lawn", "Yard", "Garden", "Yard", "Estate"]
parkcentrepiecelist = ["Fountain", "Statue", "Great tree", "Monument", "Lake", "Playground", "Gazebo", "Maze", "Flowerbed"]

universitynamelist = ["University", "Academy", "School", "College", "Institute"]
	
with open("innnamespart2.txt") as f:
    nounlist = f.read().splitlines() 	
	
with open("innspeciality.txt") as f:
    fooddrinklist = f.read().splitlines() 
	
with open("medievalsmells.txt") as f:
    smelllist = f.read().splitlines() 
	
with open("femalename.txt", encoding='latin-1') as f:
    humannamelist = f.read().splitlines()
	
with open("medievalfemalename.txt", encoding='latin-1') as f:
    humannamelist += f.read().splitlines() 
	
with open("malename.txt", encoding='latin-1') as f:
    humannamelist += f.read().splitlines() 	
	
with open("medievalmalename.txt", encoding='latin-1') as f:
    humannamelist += f.read().splitlines() 
	
with open("medievalacademicdisciplines.txt", encoding='latin-1') as f:
    disciplinelist = f.read().splitlines() 	
	
with open("fantasyacademicdisciplines.txt", encoding='latin-1') as f:
    disciplinelist += f.read().splitlines() 
	

def main(identifier = 0):

	output = {}
	
	if identifier == 0:
		if random.random() < 0.5:
			identifier = random.randint(1, 4)
		else:
			identifier = random.randint(1, len(institutionlist))
		
	output["identifier"] = identifier		
	
	if identifier == 1: #Inns
	
		output = fantasyinngenerator.main()
		
	elif identifier == 2: #Taverns
	
		output = fantasyinngenerator.main()
		if output["name"].endswith(" Inn"):
			output["name"] = output["name"][:-4]
			output["name"] += " Tavern"
			
	elif identifier == 3: #Trading Post
	
		dum = random.random()
	
		if dum < 0.33:
			output["name"] = "The " + random.choice(nounlist) + " " + random.choice(tradingnameslist)
		elif dum < 0.66:
			output["name"] = "The " + random.choice(directionslist) + " " + random.choice(tradingnameslist)
		else:
			output["name"] = random.choice(humannamelist) + "'s " + random.choice(tradingnameslist)
			
		dum = random.randint(1, 4)
		output["food"] = []
		for i in range(dum):
			output["food"].append(random.choice(fooddrinklist))
		
		output["smell"] = random.choice(smelllist)
		
	elif identifier == 4: #Temple
	
		dum = random.random()
	
		if dum < 0.20:
			output["name"] = "Saint " + random.choice(humannamelist) + "'s"
		elif dum < 0.40:
			output["name"] = "Saint " + random.choice(humannamelist) + "'s " + random.choice(templenameslist)
		elif dum < 0.60:
			output["name"] = "The " + random.choice(templeadjectivelist) + " Saint " + random.choice(humannamelist)
		elif dum < 0.80:
			output["name"] = random.choice(templenameslist) + " of @here"
		else:
			output["name"] = "@here " + random.choice(templenameslist)

		output["succour"] = random.choice(succourlist)
		
	elif identifier == 5: #Library
	
		dum = random.random()
	
		if dum < 0.1:
			output["name"] = "Saint " + random.choice(humannamelist) + "'s"
		elif dum < 0.25:
			output["name"] = "Saint " + random.choice(humannamelist) + "'s Library" 
		elif dum < 0.3:
			output["name"] = "The " + random.choice(nounlist) + " Library" 
		else:
			output["name"] = "Library of @here"
	
		dum = random.randint(1, 3)
		output["disciplines"] = []
		for i in range(dum):
			output["disciplines"].append(random.choice(disciplinelist))
			
	elif identifier == 6: #University
	
		dum = random.random()
	
		if dum < 0.15:
			output["name"] = "Saint " + random.choice(humannamelist) + "'s"
		elif dum < 0.3:
			output["name"] = "Saint " + random.choice(humannamelist) + "'s " + random.choice(universitynamelist) 
		else:
			output["name"] = random.choice(universitynamelist) + " of @here"
	
		dum = random.randint(1, 5)
		output["disciplines"] = []
		for i in range(dum):
			output["disciplines"].append(random.choice(disciplinelist))
	
	elif identifier == 7: #Park
	
		dum = random.random()
	
		if dum < 0.25:
			output["name"] = "The " + random.choice(nounlist) + " " + random.choice(parknameslist)
		elif dum < 0.50:
			output["name"] = "The " + random.choice(directionslist) + " " + random.choice(parknameslist)
		elif dum < 0.75:
			output["name"] = random.choice(humannamelist) + "'s " + random.choice(parknameslist)
		else:
			output["name"] = "@here " + random.choice(parknameslist)
	
		output["centrepiece"] = random.choice(parkcentrepiecelist)
		
	output["discriptor"] = random.choice(adjectivelist) + " " + institutionlist[identifier-1]
	output["identifier"] = identifier
		
	return(output)
		
	
		
	
		
	