import random
import randomnamegenerator
import homebrew as hb
import fantasyNPCgenerator
import fantasyinstitutiongenerator

#The output is an object with seven keys output["name"], output["gravity"], output["environment"], output["assets"], output["quirk"], output["civilization"], output["secret"]
 
with open("syfyplanetproblem.txt", encoding='latin-1') as f:
    problemlist = f.read().splitlines() 
 
with open("syfanplanetproblem.txt", encoding='latin-1') as f:
    problemlist += f.read().splitlines() 
	
with open("syfyplanetasset.txt", encoding='latin-1') as f:
    assetlist = f.read().splitlines() 
	
with open("syfanplanetasset.txt", encoding='latin-1') as f:
    assetlist += f.read().splitlines() 	
	
with open("syfyplanetoddity.txt", encoding='latin-1') as f:
    odditylist = f.read().splitlines() 
	
with open("syfanplanetoddity.txt", encoding='latin-1') as f:
    odditylist += f.read().splitlines() 	
	
with open("starname.txt", encoding='latin-1') as f:
    namelist = f.read().splitlines()
	
governmenttypelist = ["anarchy", "democracy", "corporation oligarchy",\
	"technological oligarchy", "AI government", "retired government",\
	"captive government", "balkan states", "civil service bureaucracy",\
	"dictatorship", "monarchy", "religious oligarchy", "feudal government"]

governmentadjectivelist = ["a popular", "a successful", "a unpopular", "a adequate",\
	"a impersonal", "an outdated", "a model", "an ideal", "a experimental", "a strict",\
	"a revolutionary", "a benevolent", "a corrupt", "a traditional", "a failing"]
	
	
	
def main(arg1 = None, arg2 = None):
# Generates a random planet from tables and RNGs, the output is an object
#The input selects the size 0: Random, 1:Outpost, 2:Village, 3:Town, 4:City

	problemlist = []
	
	output = {}
	
	output["error"] = None
	
	if arg2 not in [None, "land", "water", "gas", "overpopulated", "populated", "uninhabited"]: 
		output["error"]  = "Incorrect input"
	

	
	rnd = random.random()
	if rnd < 0.50:
		output["name"] = random.choice(namelist)
	else:
		output["name"] = randomnamegenerator.main()
		
	rnd = random.random()
	if rnd < 0.97:
		output["sol"] = str(random.randint(7, 40)) + " hours"
	else:
		output["sol"] = "Tidally locked"
	
			
			
		
		#-----------------------
		#~~~~~~Planet type~~~~~~
		#-----------------------
		
	rnd = random.random()
	if rnd < 0.7:
		planettype  = 1 # land planet
	elif rnd < 0.9:
		planettype  = 2 # water planet
	else:
		planettype  = 3 # gas planet
		
	if arg1 == "land":
		planettype  = 1 # land planet
	elif arg1 == "water":
		planettype  = 2 # water planet
	elif arg1 == "gas":
		planettype  = 3 # gas planet
	
	if arg2 == "land":
		planettype  = 1 # land planet
	elif arg2 == "water":
		planettype  = 2 # water planet
	elif arg2 == "gas":
		planettype  = 3 # gas planet

	
	if planettype  == 1:
		# land planet
		
		nature = random.choice(["planet", "continental planet", "world",\
		"terrestrial planet", "telluric planet", "rocky planet", "rocky world"])
		
		# gravity 
		rnd2 = random.random()
		if rnd2 < 0.50:
			output["gravity"] = str(hb.sigfig(1/3 + random.random() * 2 / 3, 2)) + " g"
		else:
			output["gravity"] = str(hb.sigfig(1 + (random.random() * 2)**3, 2)) + " g"

		
		environmentlist = ["Tundras", "Taigas", "Forests", "Grasslands", "Deserts", "Jungles",\
		"Ice plains", "Mountains", "Swamps", "Volcanoes", "Levitating islands", "Islands",\
		"Underwater cave system", "Cave system", "Ruins", "Nuclear wasteland", "Savannah"]
		
		output["environment"] = []
		n = random.randint(1, 10)
		for x in range(0, n):
			output["environment"].append(environmentlist.pop(random.randrange(len(environmentlist))))
			
		rnd2 = random.random()
		if rnd2 < 0.30: 
			populated = 3 #overpopulated
		elif rnd2 < 0.80:
			populated = 2 #populated
		else:	
			populated = 0 #uninhabited
			
		assetlist.extend(["Unique flora", "Unique fauna", "Tasty flora", "Tasty fauna",\
			"Flora with medical uses", "Fauna with medical uses", "Fertile underwater Land", \
			"Flora with military uses", "Fauna with military uses",\
			"Flora with unexplained capacity", "Fauna with unexplained capacity"\
			])
			
		odditylist.extend(["Sweet smell in the atmosphere", "Colorful water", \
			"Very large flora", "Very large fauna", "Cyclical food chain",\
			"Fauna with unique breeding method", "Presence of an intelligent hive mind",\
			"Strongly symbiotic ecosystem", "No large flora", "No large fauna"])

		problemlist.extend(["Toxins in the atmosphere", "Toxic water", \
			"Very dangerous flora", "Very dangerous fauna", "Poisonous wildlife",\
			"Presence of an intelligent and dangerous hive mind",\
			"Very delicate ecosystem", "No flora", "No fauna", "No wildlife"])
			
		odditylist.extend(["Mercury lakes",\
			"The continents travel a few meters a day, all maps are carefully dated"])
			

			
	if planettype  == 2:
		
		# waterworld
		
		nature = random.choice(["water planet", "ocean planet", "water world",\
		"aquaplanet", "panthalassic planet", "ocean world"])
		
		# gravity 
		rnd2 = random.random()
		if rnd2 < 0.50:
			output["gravity"] = str(hb.sigfig(1/3 + random.random() * 2 / 3, 2)) + " g"
		else:
			output["gravity"] = str(hb.sigfig(1 + (random.random() * 2)**3, 2)) + " g"

		
		environmentlist = ["Islands", "Artificial islands", "Coral reefs", "Open ocean",\
		"Ice plains", "Submarine volcanoes", "Ruins", "Seaweed forests", \
		"Underwater cave system", "Seaweed meadows", "Deep sea", "Salt marches"]
		
		output["environment"] = []
		n = random.randint(1, 7)
		for x in range(0, n):
			output["environment"].append(environmentlist.pop(random.randrange(len(environmentlist))))
			
		rnd2 = random.random()
		if rnd2 < 0.05: 
			populated = 3 #overpopulated
		elif rnd2 < 0.60:
			populated = 2 #populated
		else:	
			populated = 0 #uninhabited
			
		assetlist.extend(["Unique flora", "Unique fauna", "Tasty flora", "Tasty fauna",\
			"Flora with medical uses", "Fauna with medical uses", "Fertile underwater Land", \
			"Flora with military uses", "Fauna with military uses",\
			"Flora with unexplained capacity", "Fauna with unexplained capacity"\
			])
			
		odditylist.extend(["Sweet smell in the atmosphere", "Colorful water", \
			"Very large flora", "Very large fauna", "Cyclical food chain",\
			"Fauna with unique breeding method", "Presence of an intelligent hive mind",\
			"Strongly symbiotic ecosystem", "No large flora", "No large fauna"])

		problemlist.extend(["Toxins in the atmosphere", "Toxic water", \
			"Very dangerous flora", "Very dangerous fauna", "Poisonous wildlife",\
			"Presence of an intelligent and dangerous hive mind",\
			"Very delicate ecosystem", "No flora", "No fauna", "No wildlife"])
			
		assetlist.extend(["Powerful and stable currents" \
			])
			
		odditylist.extend(["City sized wale like creatures with complicated ecosystems inside" \
			])
		
	if planettype  == 3:
		# gas planet
		
		nature = random.choice(["gas planet", "failed star", "gas dwarf",\
		"gas giant", "helium planet", "puffy planet"])
		
		# gravity
		output["gravity"] = "Varies"

		
		environmentlist = ["Floating islands", "Large particulates", "No particulates", "Surface",\
		"Liquid particulates", "Ruins", "Artificial islands"]
		
		output["environment"] = []
		n = random.randint(1, 4)
		for x in range(0, n):
			output["environment"].append(environmentlist.pop(random.randrange(len(environmentlist))))
			
		rnd2 = random.random()
		if rnd2 < 0.02: 
			populated = 3 #overpopulated
		elif rnd2 < 0.25:
			populated = 2 #populated
		else:	
			populated = 0 #uninhabited
			
		assetlist.extend(["Natural flora", "Natural fauna", "Natural wildlife", 
			"Flora with unexplained capacity", "Fauna with unexplained capacity",\
			"Breathable air", "Survivable pressure", "Powerful and stable air currents",\
			"Large water source"])
			
		odditylist.extend(["City sized wale like creatures with complicated ecosystems inside",\
		"Powerful and chaotic air currents", "Areas of explosive gazes"])

		problemlist.extend(["Highly radioactive core", "Frequent dangerous storms", \
			"Very dangerous flora", "Very dangerous fauna", "Corrosive atmosphere"])
			
		
		#-----------------------
		#~~~~~~Population~~~~~~
		#-----------------------
		
	if arg1 == "overpopulated":
		populated  = 3 # overpopulated planet
	elif arg1 == "populated":
		planettype  = 2 # populated planet
	elif arg1 == "uninhabited":
		planettype  = 0 # uninhabited planet
	
	if arg2 == "overpopulated":
		populated  = 3 # overpopulated planet
	elif arg2 == "populated":
		planettype  = 2 # populated planet
	elif arg2 == "uninhabited":
		planettype  = 0 # uninhabited planet
	
		
	if populated == 3: #overpopulated
		state = random.choice(["an ultra urbanised", "a densely populated",\
		"a heavily populated", "an overpopulated", "a crowded", "a swarming"])
		
		assetlist.extend(["Patriotic population", "Good moral", "Highly educated population",\
			"Healthy population", "Extremely lawful population", "Great collection of art",\
			"Great repository of knowledge", "Perfect infrastructure", "Popular spaceport",\
			"Great night life", "Cheap food supply line",\
			"Extremely advanced medicine", "Wonderful welfare", "Fantastic theater",\
			"A renowned academy", "Renowned research center", "Efficient bureaucracy",\
			"Effective judicial system", "Uniformly morale population", "Advanced technology"\
			, "Widespread prosperity", "Acclaimed tax laws"])
			
		odditylist.extend(["Religious Population", "Extensive bureaucracy", "Distinctive architecture",\
			"Distinctive fashion", "Eccentric laws", "Strict traditions", "Timid population", "Welcoming population",\
			"Boisterous population", "Most of the population is obsessed with a specific sport.", \
			"Most of the population is obsessed with 21st century earth.",\
			"Most of the population is obsessed with medieval earth.",\
			"Most of the population is obsessed with a specific color.",\
			"Most of the population is obsessed with a recent book.",\
			"The opera is very popular", "The population as a great dislike of cybernetics",\
			"Nearly everyone has cybernetics", "Pets with a cybernetic link to the owner are very popular.",\
			"Recent change in government"\
			])
		
		problemlist.extend(["Traitors population", "Low moral", "Uneducated population", "Sickly population",\
			"Extremely criminal population", "No real culture", "Popular obscurantist movement",\
			"Archaic infrastructure", "Decaying spaceport", "No night life", "Expensive food",\
			"Primitive medicine", "No welfare", "Wide spread poverty", "Horrendous wealth distribution",\
			"No scientific community", "Cumbersome bureaucracy", "Corrupt tax laws",\
			"Archaic judicial system", "Uniformly selfish population", "Social tensions", "Segregation",\
			"Social warfare", "Bloody crime on war", "Primitive technology", "Wide spread drug addiction",])
			
		odditylist.extend(["Most of the population lives in a virtual world."\
			])
			
		problemlist.extend(["Real estate meltdown", "Extreme amounts of homelessness", "Famine"])
		
	elif populated == 2: #populated
		state = random.choice(["a lightly populated", "a rural",\
		"a sparsely populated", "a moderately populated", \
		"a inhabited",\
		"a populated"])
		
		assetlist.extend(["Patriotic population", "Good moral", "Highly educated population",\
			"Healthy population", "Extremely lawful population", "Great collection of art",\
			"Great repository of knowledge", "Perfect infrastructure", "Popular spaceport",\
			"Great night life", "Cheap food supply line",\
			"Extremely advanced medicine", "Wonderful welfare", "Fantastic theater",\
			"A renowned academy", "Renowned research center", "Efficient bureaucracy",\
			"Effective judicial system", "Uniformly morale population", "Advanced technology"\
			, "Widespread prosperity", "Acclaimed tax laws"])
			
		odditylist.extend(["Religious Population", "Extensive bureaucracy", "Distinctive architecture",\
			"Distinctive fashion", "Eccentric laws", "Strict traditions", "Timid population", "Welcoming population",\
			"Boisterous population", "Most of the population is obsessed with a specific sport.", \
			"Most of the population is obsessed with 21st century earth.",\
			"Most of the population is obsessed with medieval earth.",\
			"Most of the population is obsessed with a specific color.",\
			"Most of the population is obsessed with a recent book.",\
			"The opera is very popular", "The population as a great dislike of cybernetics",\
			"Nearly everyone has cybernetics", "Pets with a cybernetic link to the owner are very popular.",\
			"Recent change in government"\
			])
		
		problemlist.extend(["Traitors population", "Low moral", "Uneducated population", "Sickly population",\
			"Extremely criminal population", "No real culture", "Popular obscurantist movement",\
			"Archaic infrastructure", "Decaying spaceport", "No night life", "Expensive food",\
			"Primitive medicine", "No welfare", "Wide spread poverty", "Horrendous wealth distribution",\
			"No scientific community", "Cumbersome bureaucracy", "Corrupt tax laws",\
			"Archaic judicial system", "Uniformly selfish population", "Social tensions", "Segregation",\
			"Social warfare", "Bloody crime on war", "Primitive technology", "Wide spread drug addiction"])
	

	else: #uninhabited
		state = random.choice(["a uninhabitable", "a uninhabited", "a deserted",\
			"a forsaken", "an abandoned", "a wild", "a ravaged", "a devastated", "a savage",\
			"a desolate"])
			
		assetlist.extend(["Successful research station", "Brand new research station",\
			"Well built shelters for travelers", "A full spaceport for exports", "Luxury hotel",\
			"Reputed wildlife resort"\
			])
			
		odditylist.extend(["A people once inhabited this planet, nobody knows what happened to them."\
			, "Is the site for a experimental AI settlement"])
			
		problemlist.extend(["Something about the planet tends to make people go mad."])
		
	output["problem"] = str(random.choice(problemlist))
	output["asset"] = str(random.choice(assetlist))
	output["oddity"] = str(random.choice(odditylist))	
	output["descriptor"] = state + " " + nature
	
	
		#-----------------------
		#~~~~~~Government~~~~~~
		#-----------------------
		
	if populated > 0:
	
		output["government"] = str(random.choice(governmentadjectivelist))\
			+ " " + str(random.choice(governmenttypelist))
			
	else:
		
		output["government"] = None
			
		


	return(output)
   