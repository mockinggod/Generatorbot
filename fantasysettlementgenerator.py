import random
import randomnamegenerator
import homebrew as hb
import racemanagement as rm
import numpy as np
import fantasyNPCgenerator
import fantasyinstitutiongenerator
import names

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

counciladjectivelist = ["a bickering", "a cruel", "a weak", "a greedy", "a wise", "an eccentric",\
	"a confusing", "a brutal", "a cunning", "a stern", "a secretive", "a drunkard", "a zealous",\
	"a fanatical", "a pious", "a chaotic", "a methodical", "a virtuous", "a righteous", "a upstanding",\
	"a honourable", "a crooked", "a nefarious", "a squabbling", "an anarchic", "a powerless", \
	"an antiquated", "an archaic", "a brand new", "a recently appointed", "a respected", "a esteemed"]
	
rulerlist = [["despot", "despot"], ["elder", "elder"], ["mayor", "mayor"], ["grand druid", "grand druid"],
	["commander", "commander"], ["hight merchant", "hight merchant"], ["earl", "earl"], ["master", "master"],\
	["hight priest", "hight priestess"], ["crime lord", "crime lord"], ["lord", "lady"], ["count", "countess"],\
	["commissioner", "commissioner"], ["earl marshal", "earl marshal"], ["grand master", "grand master"],  \
	["merchant lord", "merchant lady"], ["shaman", "shaman"],  ["alderman", "alderwoman"]]
	
	
def main(races = [],race = None, ethnicity = "eng", size = 0):
# Generates a random settlement from tables and RNGs, the output is an object
#The input selects the size 0: Random, 1:Outpost, 2: Hamlet, 3:Village, 4:Town, 5:City

	output = {}
	size = int(size)
	output["ethnicity"] = "eng"
	if races == []:
		output["race"] = ""
		maxsize = 5
		minsize = 1
	else:
		if race is None:
			sumw = 0.0
			for ra in races:
				if ra["maxsettlement"]>=0:
					sumw += float(ra['weight'])
				
			rand = random.random()*sumw
			dum = 0
			for ra in races:
				if ra["maxsettlement"]>=0:
					dum += float(ra['weight'])
				if rand < dum:
					output["race"] = ra['racename']	
					maxsize = max(1, min(5, int(ra['maxsettlement'])))
					minsize = max(1, int(ra['maxsettlement'])-4)
					break
		else: 
			output["race"] = race
			ra = rm.exracebyn(races, race)
			ra = np.random.choice(ra)
			maxsize = max(1, min(5, int(ra['maxsettlement'])))
			minsize = max(1, int(ra['maxsettlement'])-4)
			
	if size == 0:
		setsizeweight = np.array([2.0, 3.0, 3.0 ,2.0, 1.0])
		setsizeweight = setsizeweight[minsize-1: maxsize-1]
		setsizeweight = setsizeweight/sum(setsizeweight)
		
		if minsize == maxsize:
			size = minsize
		else:
			size = np.random.choice(range(minsize,maxsize),p=setsizeweight)
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
			
	
	
	if random.random() < 0.85:
	
		tempraces = []
	
		if random.random() < 0.96:
		
			
			if races  == []:
				output["ethnicity"] = ethnicity
			else:
				tempraces = rm.exracebyn(races, output["race"])
		
		else:
		
			if races  == []:
		
				output["ethnicity"] = np.random.choice(names.humanethnicities)
				
			else:

				tempraces = rm.exracebys(races, size)

		output["ruler"] = fantasyNPCgenerator.main(tempraces, output["ethnicity"])	
		output["ruler"]["individual"] = True 
		
		if output["ruler"]["gender"] == "female":
			output["ruler"]["occupation"] = random.choice(rulerlist)[1]
		else:
			output["ruler"]["occupation"] = random.choice(rulerlist)[0]
	
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
		output["ruler"]["title"] = str(random.choice(councillist))
		ruler = output["ruler"]["title"]
		output["ruler"]["adjective"] = str(random.choice(counciladjectivelist))
		
	institutionnum = random.randint(round(size/2.1)+1, size)
	if institutionnum > 3:
		institutionnum = 4
	output["institutions"] = []
	for i in range(institutionnum):
		output["institutions"].append(fantasyinstitutiongenerator.main())
		output["institutions"][i]["name"] = output["institutions"][i]["name"].replace("@here", output["name"])
	
	for institutcheck in output["institutions"]:
		for i in range(institutionnum):	
			if output["institutions"][i]["name"] == institutcheck["name"]:
				if output["institutions"][i] != institutcheck:		
					output["institutions"].pop(i)
					break
					
					
		
	output["problem"] = str(random.choice(problemlist))
	output["asset"] = str(random.choice(assetlist))
	output["oddity"] = str(random.choice(odditylist))
	output["sizenum"] = size
	
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
   