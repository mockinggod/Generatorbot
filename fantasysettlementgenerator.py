import random
import randomnamegenerator
import homebrew as hb
import fantasyNPCgenerator
import fantasyinstitutiongenerator

#The output is an object with seven keys output["name"], output["age"], output["characteristic"], output["trait"], output["occupation"], output["gender"], output["secret"]
 
with open("medievalsettlementproblem.txt", encoding='UTF-8') as f:
    problemlist = f.read().splitlines() 
 
with open("fantasysettlementproblem.txt", encoding='UTF-8') as f:
    problemlist += f.read().splitlines() 
	
with open("medievalsettlementasset.txt", encoding='UTF-8') as f:
    assetlist = f.read().splitlines() 
	
with open("fantasysettlementasset.txt", encoding='UTF-8') as f:
    assetlist += f.read().splitlines() 	
	
with open("medievalsettlementoddity.txt", encoding='UTF-8') as f:
    odditylist = f.read().splitlines() 
	
with open("fantasysettlementoddity.txt", encoding='UTF-8') as f:
    odditylist += f.read().splitlines() 	
	
with open("medievalsettlementname.txt", encoding='UTF-8') as f:
    namelist = f.read().splitlines()
	
with open("medievalsettlementnamep1.txt", encoding='UTF-8') as f:
    namelist1 = f.read().splitlines()
	
with open("medievalsettlementnamep2.txt", encoding='UTF-8') as f:
    namelist2 = f.read().splitlines()
	
councillist = ["religious council", "council of guild leaders", "noble parlement", "magic council", "mixed council", "council of elders", "military council"]

counciladjectivelist = ["A bickering", "A cruel", "A weak", "A greedy", "A wise", "An eccentric",\
	"A confusing", "A brutal", "A cunning", "A stern", "A secretive", "A drunkard", "A zealous",\
	"A fanatical", "A pious", "A chaotic", "A methodical", "A virtuous", "A righteous", "A upstanding",\
	"A honourable", "A crooked", "A nefarious", "A squabbling", "An anarchic", "A powerless", \
	"An antiquated", "An archaic", "A brand new", "A recently appointed", "A respected", "A esteemed"]
	
rulerlist = [["Despot", "Despot"], ["Elder", "Elder"], ["Mayor", "Mayor"], ["Grand druid", "Grand druid"],
	["Commander", "Commander"], ["Hight merchant", "Hight merchant"], ["Earl", "Earl"], ["Master", "Master"],\
	["Hight priest", "Hight priestess"], ["Crime lord", "Crime lord"], ["Lord", "Lady"], ["Count", "Countess"],\
	["Commissioner", "Commissioner"], ["Earl Marshal", "Earl Marshal"], ["Grand Master", "Grand Master"],  \
	["Merchant lord", "Merchant lady"], ["Shaman", "Shaman"],  ["Alderman", "Alderwoman"]]
	
	
def main(size = 0):
# Generates a random settlement from tables and RNGs, the output is an object
#The input selects the size 0: Random, 1:Outpost, 2:Village, 3:Town, 4:City

	output = {}
	size = int(size)
	if size == 0:
		rand = random.random()
		size = 1
		if rand < 0.87:
			size = 2
			if rand < 0.65:
				size = 3
				if rand < 0.30:
					size = 4
					if rand < 0.15:
						size = 5
						
						
	if size == 1:
		output["population"] = random.randint(6, 20)
	elif size == 2:
		output["population"] = random.randint(21, 100)
	elif size == 3:
		output["population"] = random.randint(101, 400)
	elif size == 4:
		output["population"] = random.randint(401, 2500)
	elif size == 5:
		output["population"] = random.randint(2501, 30000)
	
	output["population"] = hb.sigfig(output["population"], 3)
	dummy = ["Outpost", "Hamlet", "Village", "Town", "City"]
	output["size"] = dummy[size-1]	
	
	
	rnd = random.random()
	if rnd < 0.55:
		output["name"] = random.choice(namelist)
	elif rnd < 0.70:
		output["name"] = random.choice(namelist1) + "-" + random.choice(namelist2)
	elif rnd < 0.90:
		output["name"] = random.choice(namelist1) + random.choice(namelist2).lower()
	else:
		output["name"] = randomnamegenerator.main()
			
	if random.random() < 0.97:			
		output["age"] = random.randint(0, 300) + (size-1) * random.randint(10, 250)
	else:
		output["age"] = "Unknown"
		
	
	
	if random.random() < 0.85:

		output["ruler"] = fantasyNPCgenerator.main()
		output["ruler"]["individual"] = True 
		
		if output["ruler"]["gender"] == "male":
			output["ruler"]["occupation"] = random.choice(rulerlist)[0]
		else:
			output["ruler"]["occupation"] = random.choice(rulerlist)[1]
	
		ruler = output["ruler"]["occupation"]
		if output["ruler"]["occupation"] == "Elder":
			output["ruler"]["age"] = ""
	else:
		output["ruler"] = {}
		output["ruler"]["individual"] = False
		if random.random() < 0.85:
			output["ruler"]["number"] = random.randint(2, 14)
		else:
			output["ruler"]["number"] = random.randint(15, 30)
		if output["ruler"]["number"] > output["population"]/2:
			output["ruler"]["number"] = round(output["population"]/2)
		output["ruler"]["title"] = str(random.choice(councillist))
		ruler = output["ruler"]["title"]
		output["ruler"]["adjective"] = str(random.choice(counciladjectivelist))
		
	institutionnum = random.randint(round(size/2.1)+1, size)
	if institutionnum > 3:
		institutionnum = 3
	output["institutions"] = []
	for i in range(institutionnum):
		output["institutions"].append(fantasyinstitutiongenerator.main())
		output["institutions"][i]["name"] = output["institutions"][i]["name"].replace("@here", output["name"])
	
	for institutcheck in output["institutions"]:
		for i in range(institutionnum):	
			if output["institutions"][i]["name"] == institutcheck["name"]:
				if output["institutions"][i] != institutcheck:		
					print(output["institutions"][i]["name"])
					output["institutions"].pop(i)
					break
					
					
		
	output["problem"] = str(random.choice(problemlist))
	output["asset"] = str(random.choice(assetlist))
	output["oddity"] = str(random.choice(odditylist))
	
	output["problem"] = output["problem"].replace("@settlement@", str(output["size"]), 4)	
	output["asset"] = output["asset"].replace("@settlement@", str(output["size"]), 4)
	output["oddity"] = output["oddity"].replace("@settlement@", str(output["size"]), 4)
	
	output["problem"] = output["problem"].replace("@ruler@", str(ruler), 4)	
	output["asset"] = output["asset"].replace("@ruler@", str(ruler), 4)
	output["oddity"] = output["oddity"].replace("@ruler@", str(ruler), 4)
	
	
	output["asset"] = output["asset"].lower()
	output["oddity"] = output["oddity"].lower()
	
	output["asset"] = output["asset"].capitalize()
	output["oddity"] = output["oddity"].capitalize()
	
	return(output)
   