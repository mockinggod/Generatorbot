import fantasyNPCgenerator
import randomnamegenerator
import missiongenerator
import inngenerator
import insultgenerator
import fantasyinngenerator
import fantasysettlementgenerator
import fantasybookgenerator
import syfanplanetgenerator
import riddlegenerator
import weathergenerator
import medievalshipnamegenerator
import names

import psqlfunctions as psqlf
import homebrew as hb
import racemanagement as rm
import numpy as np
from titlecase import titlecase

	
taglist = (hb.arrayreader("universaltags.txt"))


def main(ctx, races, item, *args):
	arg = []
	for input in args:
		arg.append(input)
		
		
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Genre prep
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/

	dum = []

	if item in ["fantasynpc", "fnpc", "fantasyinn", "finn", "fantasysettlement", "fsettlement", "fset", "fantasybookcase", "fbookcase", "fbc", "fantasybook", "fbook"]:
	
	
		for race in races:
			if race["genre"] == 'fantasy':
				dum.append(race)
		

	races = dum
		

# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Names
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/

	if item == "name" or item  =="n":
	
		numloop = 1
		types = []
		openoutput = ""
		typelist = []
		typelist.extend(names.ethnicities)
		typelist.extend(["random", "r", "settlement", "set", "inn", "ship", "book"])
		full = False
		gender = None
		gen = False
		lenght = [4,10]
		
		for input in arg:
			try: 
				int(input)
				integer = True
			except ValueError:
				integer = False
			if integer:
				numloop = int(input)
			else: 
				if input == 'full' or input == 'fullname':
					full = True
				elif input == 'female' or input == 'f':
					gender = 'female'
				elif input == 'male' or input =='m':
					gender = 'male'
				elif input == 'surname' or input == 'sur' or input == 's':
					full = True
					gender = 'surname'
				elif input == 'short':
					lenght = [2,6]
				elif input == 'long':
					lenght = [9,15]
				elif input == 'endless':
					lenght = [12,22]
				elif input in typelist:
					types.append(input)
				else:
					openoutput += "Unknown name type: " + input + " so ignored\n"
				
		for i in range(numloop):
		
	
			if len(types) == 0: 
				type = "eng"
			else:
				type = np.random.choice(types)			

			if type == "random" or type == "r" :
					
				openoutput += names.randname(lenght) 
				
				if full:
				
					openoutput += " " + names.randname(lenght) + "\n"
					
				else:
				
					openoutput += "\n"
					
			
	
			elif type in names.ethnicities:
					
				if type in names.humangentypelist:
					gen = True
					
				#easter egg for a friend 
				if ctx.message.author.id == int(132528782794817536) and "japan" in args:

					openoutput +="Rice"
		
				#end easter egg
			
				if gender == None:
				
					gender = np.random.choice(["male", "female"])
			
				if gender == "male":
				
					string = type + "m"

					openoutput += names.name(gen, string, lenght) + ' '
					
				elif gender == "female":
					
					string = type + "f"
					
					openoutput += names.name(gen, string, lenght) + ' '
					
				if full:

					if type in names.nosurnamelist:
				
						string = type + "m"
						
						openoutput += names.name(True, string, lenght) + "\n"
						
					else:
					
						string = type + "sur"
					
						openoutput += names.name(gen, string, lenght) + "\n"
					
				else:
				
					openoutput += "\n"
					
			elif type == "settlement" or type == "set":
		

				dum = fantasysettlementgenerator.main(races)
				openoutput += dum["name"]  + "\n"
					
			elif type == "inn":
			
				dum = fantasyinngenerator.main()
				openoutput += titlecase(dum["name"])  + "\n"

					
			elif type == "ship":

				openoutput += medievalshipnamegenerator.main()  + "\n"
					
			elif type == "book" or type == "b":
				
				dum = fantasybookgenerator.main()
				openoutput += titlecase(dum["title"]) + "\n"
						
				
			else: 
			
				openoutput +=  "Errorname: mybad\n"

				
				
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Titles
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/

		
	elif item == "booktitle" or item == "btitle":
		openoutput = ""
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			dum = fantasybookgenerator.main()
			openoutput += titlecase(dum["title"]) + "\n"
		
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					NPCS
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
		
	elif item == "fantasynpc" or item == "fnpc":
	#Generates a fantasy NPC.
		numloop = 1

		race = None
		job = None
		ethnicity = 'eng'
	
		for input in arg:
			try: 
				int(input)
				integer = True
			except ValueError:
				integer = False
			if integer:
				numloop = int(input)
			else: 
				if any(input == ra['racename'] for ra in races):
					race = input
				elif input in names.ethnicities:
					ethnicity = input
				else:
					job = input
					
		openoutput = ""
		secretoutput = ""
		
		if race == None:
			tempraces = races
		else:
			tempraces = []
			for ra in races:
				if race == ra['racename']:
					tempraces.append(ra)
				
		for i in range(numloop):
		
			NPC = fantasyNPCgenerator.main(tempraces, ethnicity, job)
				
			openoutput += str(charaformat(NPC)) + "\n\n"
				
			secretoutput += str(secretcharaformat(NPC)) + "\n\n"
		
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Inns
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
		
	elif item == "fantasyinn" or item == "finn":
	
		tempraces = rm.exracebys(races, 2)
	
		numloop = 1
		ethnicity = "eng"
		for input in arg:
			try: 
				int(input)
				integer = True
			except ValueError:
				integer = False
			if integer:
				numloop = int(input)
			else: 
				if input in names.ethnicities:
					ethnicity = input
				

	
		openoutput = ""
		secretoutput = ""
		
		for i in range(numloop):		
			
			inn = fantasyinngenerator.main()
			output = "\n**" + inn["name"] + "**\nOddity: " + inn["oddity"]   \
				 + "\nSpeciality: " + inn["specialty"]
			openoutput += output
			
			output += "\nSecret: " + inn["secret"]
			secretoutput += output
			
			owner = fantasyNPCgenerator.main(tempraces, ethnicity, "Innkeeper")
			waiter = fantasyNPCgenerator.main(tempraces, ethnicity, "Waiter")
			

			openoutput += "\n\n" + owner["name"] +":"+ " A" + owner["age"] + " "+ str(owner["gender"]) +\
				" "+ str(owner["race"]) + " owner\nCharacteristic: " + owner["characteristic"]
			if waiter["gender"] == "female":
				openoutput += "\n\n" + waiter["name"] +":"+ " A" + waiter["age"] + " "+ str(waiter["gender"]) +\
					" "+ str(waiter["race"]) + " waitress\nCharacteristic: " + waiter["characteristic"]
			else:
				openoutput += "\n\n" + waiter["name"] +":"+ " A" + waiter["age"] + " "+ str(waiter["gender"]) +\
					" "+ str(waiter["race"]) + " waiter\nCharacteristic: " + waiter["characteristic"]	

			openoutput += "\n"
				
			secretoutput +=  "\n\n" + owner["name"] +":"+ " A" + owner["age"] + " "+ str(owner["gender"]) +\
				" "+ str(owner["race"]) + " owner\nCharacteristic: " + owner["characteristic"] + "\nTrait: " + owner["trait"]
			if owner["secret"] != "Has no secret":
				secretoutput += "\nSecret: " + owner["secret"]
			if waiter["gender"] == "female":
				secretoutput +=  "\n\n" + waiter["name"] +":"+ " A" + waiter["age"] + " "+ str(waiter["gender"]) +\
					" "+ str(waiter["race"]) + " waitress\nCharacteristic: " + waiter["characteristic"] + "\nTrait: " + waiter["trait"]
			else:
				secretoutput +=  "\n\n" + waiter["name"] +":"+ " A" + waiter["age"] + " "+ str(waiter["gender"]) +\
					" "+ str(waiter["race"]) + " waiter\nCharacteristic: " + waiter["characteristic"] + "\nTrait: " + waiter["trait"]
			if waiter["secret"] != "Has no secret":
				secretoutput += "\nSecret: " + waiter["secret"] + "\n"

			secretoutput += "\n"
		
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Missions
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
		
	elif item == "mission" or item == "mis" or item == "m":
			#Generates a mission.
			
		if len(arg) == 0:
			mission = missiongenerator.main()
		else:
			mission = missiongenerator.main(int(arg[0]))
		
		output = "Difficulty: " + str(mission["difficulty"]) + "\nObjective: \n"
		i = 0
		while i < len(mission["objectives"]):
			output += "   * " + mission["objectives"][i-1] + "\n"
			i += 1
		
		output += "Reward: " + str(mission["reward"]) + "\n"
		
		if len(mission["opencomplications"]) > 0:
			output += "Complications: \n" 
			i = 0
			while i < len(mission["opencomplications"]):
				output += "   * " + mission["opencomplications"][i] + "\n"
				i += 1

		openoutput = output

		if len(mission["secretcomplications"]) > 0:	
			output += "Secret complications: \n"
			i = 0
			while i < len(mission["secretcomplications"]):
				output += "   * " + mission["secretcomplications"][i-1] + "\n"
				i += 1
		secretoutput = output
		
	elif item == "jobboard" or item == "jb":
	
		if len(arg) == 0:
			arg.append(5)
			
		openoutput = "**Job Board**\n"
		secretoutput = "**Job Board**\n"
	
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			
			
			mission = missiongenerator.main()
			
			output = "\n__Job: " + str(loop) + "/" + str(arg[0]) + "__\nDifficulty: " + str(mission["difficulty"]) + "\nObjective: \n"
			i = 0
			while i < len(mission["objectives"]):
				output += "   * " + mission["objectives"][i] + "\n"
				i += 1
			
			output += "Reward: " + str(mission["reward"])
			if len(mission["opencomplications"]) > 0:
				output += "\nComplications:" 
				i = 0
				while i < len(mission["opencomplications"]):
					output += "\n   * " + mission["opencomplications"][i]
					i += 1
			openoutput += output + "\n"
			
			if len(mission["secretcomplications"]) > 0:	
				output += "\nSecret complications: "
				i = 0
				while i < len(mission["secretcomplications"]):
					output += "\n   * " + mission["secretcomplications"][i]
					i += 1
			secretoutput += output + "\n"
			output = ""
			
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Settlements
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/

			
	elif item == "fantasysettlement" or item == "fsettlement" or item == "fset": #fantasy settlement
		
		size = 0
		race = None
		ethnicity = 'eng' 
		
		for input in arg:
			try: 
				int(input)
				integer = True
			except ValueError:
				integer = False
			if integer:
				size = int(input)
			else: 
				if any(input == ra['racename'] for ra in races):
					race = input
				elif input in names.ethnicities:
					ethnicity = input
		

		if size > 5 or size < 0:
			openoutput = "The input must be a number between 1 and 5, see itemlist for more info"
		else:			
			set = fantasysettlementgenerator.main(races, race, ethnicity, size)
			openoutput, secretoutput = fantasysettlementformat(races, set)


		
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Books
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/

	elif item == "fantasybook" or item == "fbook": #fantasy book
		book = fantasybookgenerator.main()

		if len(arg) == 0:
			arg.append(1)
			
		openoutput = ""
		secretoutput = ""
			
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			
			book = fantasybookgenerator.main()

			openoutput += "\nTitle: " + titlecase(book["title"]) +  \
			"\nAuthor: " + book["author"].title()
			#+ "\nState: " + book["state"].capitalize() doesn't fell needed, hard to fit in some contexts

			secretoutput += "\nTitle: " + titlecase(book["title"]) +  \
			"\nAuthor: " + book["author"].title() + " a " +book["authorjob"].lower()
			#+ "\nState: " + book["state"].capitalize() doesn't fell needed, hard to fit in some contexts
			
			
			secretoutput += "\nSubject: " + book["subject"].capitalize()
			secretoutput += "\nBranch: " + book["branch"].capitalize()
			secretoutput += "\nFocus: " + book["focus"].capitalize()

			if book["secret"] != "no secret":
				secretoutput += "\nSecret: " + book["secret"].capitalize()

			secretoutput += "\n"		
			openoutput += "\n"
		
		

	
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Planets
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
	
	elif item == "syfanplanet": #Syfan planet
	

	
		if len(arg) > 1:
			planet = syfanplanetgenerator.main(arg[0], arg[1])
		if len(arg) == 1:		
			planet = syfanplanetgenerator.main(arg[0])
		if len(arg) == 0:
			planet = syfanplanetgenerator.main()
				
		if planet["error"] != None:
		
			openoutput = planet["error"]
			
		else:
				
			openoutput = "__**" + planet["name"] + "**__\n"
			openoutput += "*" + planet["descriptor"].capitalize() + "*\n"
					
			if planet["government"] != None:
				openoutput += "\nGovernment: " + planet["government"].capitalize()		
			openoutput += "\nGravity: " + planet["gravity"]
			openoutput += "\nSol: " + planet["sol"] + "\n"
			
			openoutput += "Environments: \n" 
			i = 0
			while i < len(planet["environment"]):
				openoutput += "   * " + planet["environment"][i] + "\n"
				i += 1
			
			openoutput += "\nAsset: " + planet["asset"]
			openoutput += "\nOddity: " + planet["oddity"]
			openoutput += "\nProblem: " + planet["problem"]
		
			openoutput += "\n\n"
	
	# end of generator
	
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Misc
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/

	elif item == "riddle":
	
		if len(arg) == 0:
			arg.append("0")
			
		if arg[0] in ["0", "1", "2", "3", "4", "5"]:
			
			riddle = riddlegenerator.main(arg[0])
			openoutput = " " + riddle["riddle"]
			secretoutput = " " + riddle["riddle"] + "\n" + "__Answer: __" + riddle["answer"]

				
			openoutput = openoutput.replace("\\n", "\n")
			secretoutput = secretoutput.replace("\\n", "\n")	
			
		else:
			openoutput = "The difficulty rating of the riddles are between 1 and 5."

	elif item == "riddles":
	
		openoutput = ""
		secretoutput = ""
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			
			riddle = riddlegenerator.main(0)
			openoutput += " " + riddle["riddle"] + "\n\n"
			secretoutput += " " + riddle["riddle"] + "\n" + "__Answer: __" + riddle["answer"] + "\n\n"

			
		openoutput = openoutput.replace("\\n", "\n")
		secretoutput = secretoutput.replace("\\n", "\n")	
			
	elif item == "insult" or item == "insults":
	
		valid = True
		argslist = ["default", "empty", "empty"]

		test = 0
		numloop = 1		
		if len(arg) > 0:
			track = 0
			for input in arg:
				try: 
					int(input)
					integer = True
				except ValueError:
					integer = False
				if integer:
					numloop = int(input)
				elif isinstance(input, str):
					if input in "intelligence":
						dum = "intelligence"
						test += 1
					if input in "character":
						dum = "character"
						test += 1
					if input == "looks":
						dum = "appearance"
						test += 1
					if input in "appearance":
						dum = "appearance"
						test += 1
					if input in "miscellaneous":
						dum = "misc"
						test += 1
					if input in "comeback":
						dum = "comeback"
						test += 1
					argslist[track] = dum
					track += 1
					if test > 1:
						openoutput = "Could not recognize this type of insult"
						valid = False
				else:
					openoutput = "Insult items need either strings or integer"
					valid = False
	
		if valid:
			openoutput = ""
			args = (argslist[0], argslist[1], argslist[2])
			loop = 0
			while loop < numloop:
				loop += 1
				
				openoutput += insultgenerator.main(*args) + "\n"
				
	elif item == "weather" or item == "w":
	
		if len(arg) == 0:
			arg.append(0)
			
		openoutput = weathergenerator.main(arg[0])
	
	
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Book keeping
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/

	elif item == "nothing was entered0":
		openoutput = "There must be an argument after gen, use !itemlist to get a list"
		
	else:
		openoutput = item + " is not a valid generator argument, use !itemlist to get a list"
		
	try: secretoutput
	except NameError: 
		secretoutput = openoutput
	
	if "#" in secretoutput:
		for tag in taglist:
			rand = np.random.randint(1,len(tag))
			openoutput = openoutput.replace(tag[0], tag[rand], 5)
			secretoutput = secretoutput.replace(tag[0], tag[rand], 5)
			
	if "[[" in secretoutput:
		memory = [[""]]
		
			
		split1 = secretoutput.split("[[")
		secretoutput = split1[0]
		i = len(split1)
		for j in range(1,i):
			split2 = split1[j].split("]]")
			list = split2[0].split("/")
			if list in memory:
				secretoutput += memory[0][memory.index(list)] + split2[1]
			else:
				memory.append(list)
				memory[0].append(np.random.choice(list))
				
				secretoutput +=  memory[0][-1] + split2[1]
				

		if "[[" in openoutput:
			split1 = openoutput.split("[[")
			openoutput = split1[0]
			i = len(split1)
			
			for j in range(1,i):
				split2 = split1[j].split("]]")
				list = split2[0].split("/")
				openoutput += memory[0][memory.index(list)] + split2[1]
				

	secretoutput = secretoutput.replace("   ", " ", 10)				
	secretoutput = secretoutput.replace("  ", " ", 100)	
	secretoutput = secretoutput.replace(" .", ".", 10)		
	secretoutput = secretoutput.replace(" ,", ",", 10)	
	secretoutput = secretoutput.replace(" :", ":", 10)	
	openoutput = openoutput.replace("   ", " ", 10)	
	openoutput = openoutput.replace("  ", " ", 100)	
	openoutput = openoutput.replace(" .", ".", 10)		
	openoutput = openoutput.replace(" ,", ",", 10)
	openoutput = openoutput.replace(" :", ":", 10)
	
	return(openoutput, secretoutput)
	

	
	
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Formating functions
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
	
def charaformat(character):

	output = character["name"]
	dummy = str(str(character["age"]) + " " + str(character["gender"]) + " " + str(character["race"]) + " " + str(character["occupation"]) + ".")
	output += "\nA" + dummy.lower()
	output += "\nCharacteristic: " + character["characteristic"]
		 
	openoutput = output
	
	return(openoutput)
	
def secretcharaformat(character):

	output = character["name"] 
	dummy = str(character["age"]) + " " + str(character["gender"]) + " " + str(character["race"]) + " " + str(character["occupation"]) + "."
	output += "\nA" + dummy.lower()
	output += "\nCharacteristic: " + character["characteristic"]	
	output += "\nTrait: " + character["trait"] 
	
	dummy =  character["secret"]
	if str(dummy) != str("Has no secret"):
		output += "\nSecret: " + dummy
		
	secretoutput = output
	
	return(secretoutput)
	
def fantasysettlementformat(races, settlement):
	
	# general settlement stuff
		
	output = "__**" + settlement["name"] + "**__: "
	output += settlement["race"].capitalize() + " " + settlement["size"] + "\n"
#	output += "Population: " + str(settlement["population"]) + "\n" Current philosophy goes against giving an accurate population, plus settlement have sufficient content
	
	openoutput = output
	
#	output += "Age: " + str(settlement["age"]) + "\n" Current philosophy goes against giving an accurate age
	
	secretoutput = output
	
	output = "Asset: " + settlement["asset"] + "\n"
	output += "Oddity: " + settlement["oddity"] + "\n"

	
	openoutput += output + "\n"
	
	output += "Problem: " + settlement["problem"] + "\n"
	
	secretoutput += output + "\n"	
	
	# Ruler stuff
	
	output = "__Ruler__: "
	
	if settlement["ruler"]["individual"]:
		output += settlement["ruler"]["name"] + "\nA"
		output +=  str(settlement["ruler"]["age"]) + " " + str(settlement["ruler"]["gender"]) + " " + str(settlement["ruler"]["race"]) + " " + str(settlement["ruler"]["occupation"]) + "\n"
		
		openoutput += output + "\n" 
		
		output += "Characteristic: " + settlement["ruler"]["characteristic"] + "\n"
		output += "Trait: " + settlement["ruler"]["trait"] + "\n"
		if str(settlement["ruler"]["secret"]) != str("Has no secret"):
			output += "Secret: " + settlement["ruler"]["secret"] + "\n"
			
		secretoutput += output + "\n"
		
	else:
		output += settlement["ruler"]["adjective"] + " " + settlement["ruler"]["title"]
		output += "\nNumber of membres: " + str(settlement["ruler"]["number"])
		
		openoutput += output + "\n\n"
		secretoutput += output + "\n\n"
		
	# Institutions
	
	output = "__Institutions__"
	
	for institution in settlement["institutions"]:
		output += "\n**" + institution["name"] + "**\n"
		output +=  institution["discriptor"]
		
		openoutput += output + "\n"
		secretoutput += output
		output = ""
		
		if np.random.random()<0.85:
			ethnicity = settlement["ethnicity"]
			tempraces = rm.exracebyn(races, settlement["race"])
		else:
			ethnicity = np.random.choice(names.humanethnicities)
			tempraces = rm.exracebys(races, settlement["sizenum"])
			
		if institution["identifier"] == 1 or institution["identifier"] == 2: #inn/tavern
		
			output += "\nOddity: " + institution["oddity"]   \
				 + "\nSpeciality: " + institution["specialty"]				
			output += "\nSecret: " + institution["secret"]		
			
			secretoutput += output
			output = ""
			
			owner = fantasyNPCgenerator.main(tempraces, ethnicity, "owner")
			
			secretoutput +=  "\n" + secretcharaformat(owner) + "\n"
			
			# Removed Waiter from settlement inns, too much info already
			# secretoutput += "\n__Waiter__\n" + secretcharaformat(waiter) + "\n" 
		
		elif institution["identifier"] == 3: #trading post
	
			secretoutput += "\nFood vendors:\n"
			for vendor in institution["food"]:
				secretoutput += " - " + vendor + "\n"
				
			secretoutput += "Smell: " + institution["smell"] + "\n"
			
		elif institution["identifier"] == 4: #Temple
		
			secretoutput += "\nPrincipal succour: " + institution["succour"] + "\n"
			
			highpriest = fantasyNPCgenerator.main(tempraces, ethnicity, "High priest")
			
			secretoutput += "\n" + secretcharaformat(highpriest) + "\n"
			
		elif institution["identifier"] == 5: #Library
		
			secretoutput += "\nAreas of focus:\n"
			for discipline in institution["disciplines"]:
				secretoutput += " - " + discipline + "\n"
				
			librarian = fantasyNPCgenerator.main(tempraces, ethnicity, "Librarian")
			
			secretoutput +=  "\n" + secretcharaformat(librarian) + "\n"
				
		elif institution["identifier"] == 6: #University
		
			secretoutput += "\nClasses taught:\n"
			for discipline in institution["disciplines"]:
				secretoutput += " - " + discipline + "\n"
				
			dean = fantasyNPCgenerator.main(tempraces, ethnicity, "Dean")
			
			secretoutput +=  "\n" + secretcharaformat(dean) + "\n"
			
		elif institution["identifier"] == 7: #Park
		
			secretoutput += "\nCentre piece: " + institution["centrepiece"] + "\n"
			

			
	return(openoutput, secretoutput)