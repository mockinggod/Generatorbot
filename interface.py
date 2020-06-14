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

import homebrew as hb
import numpy as np
from titlecase import titlecase

with open("femalename.txt", encoding='latin-1') as f:
    femalenamelist = f.read().splitlines() 	
	
with open("medievalfemalename.txt", encoding='latin-1') as f:
    medievalfemalenamelist = f.read().splitlines() 
	
with open("malename.txt", encoding='latin-1') as f:
    malenamelist = f.read().splitlines() 	
	
with open("medievalmalename.txt", encoding='latin-1') as f:
    medievalmalenamelist = f.read().splitlines() 
	
with open("surname.txt", encoding='latin-1') as f:
    surnamelist = f.read().splitlines() 	
	
with open("medievalsurname.txt", encoding='latin-1') as f:
    medievalsurnamelist = f.read().splitlines() 
	
taglist = (hb.arrayreader("universaltags.txt"))

def main(ctx, item, *args):
	arg = []
	for input in args:
		arg.append(input)
		

# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Names
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/

	if item == "randomname" or item == "rname":
	
		openoutput = ""
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			
			openoutput += randomnamegenerator.main() + "\n"
		
	elif item == "malename" or item == "mname":

		openoutput = ""	
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			
			openoutput += np.random.choice(malenamelist) + "\n"
		
	elif item == "femalename" or item == "fname":
	
		openoutput = ""
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			
			openoutput += np.random.choice(femalenamelist) + "\n"
		
	elif item == "surname" or item == "sname":
	
		openoutput = ""
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			openoutput += np.random.choice(surnamelist) + "\n"
			
	elif item == "settlementname" or item == "setname":
		openoutput = ""
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			dum = fantasysettlementgenerator.main()
			openoutput += dum["name"] + "\n"
			
	elif item == "innname":
		openoutput = ""
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			dum = fantasyinngenerator.main()
			openoutput += titlecase(dum["name"]) + "\n"
			
	elif item == "shipname":
		openoutput = ""
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			openoutput += medievalshipnamegenerator.main() + "\n"
		
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
		
	elif item == "fantasyNPC" or item == "fNPC":
		#Generates a fantasy NPC.
		if len(arg) == 0:
			loopmax = 1
			job = None
		else: 		
			try:
				loopmax = int(arg[0])
				job = None
			except ValueError:
				loopmax = 1
				job = arg[0]
				
		openoutput = ""
		secretoutput = ""
				
		loop = 0
		while loop < loopmax:
			loop += 1
			
			if job == None:
				NPC = fantasyNPCgenerator.main()
			else:
				NPC = fantasyNPCgenerator.main(job)
				
			openoutput += str(charaformat(NPC)) + "\n\n"
				
			secretoutput += str(secretcharaformat(NPC)) + "\n\n"
		
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Inns
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
		
	elif item == "fantasyinn" or item == "finn":
	
		openoutput = ""
		secretoutput = ""
		
		if len(arg) == 0:
			arg.append(1)
		loop = 0
		while loop < int(arg[0]):
			loop += 1
			
			inn = fantasyinngenerator.main()
			output = "\n**" + inn["name"] + "**\nOddity: " + inn["oddity"]   \
				 + "\nSpeciality: " + inn["specialty"]
			openoutput += output
			
			output += "\nSecret: " + inn["secret"]
			secretoutput += output
			
			owner = fantasyNPCgenerator.main("Innkeeper")
			waiter = fantasyNPCgenerator.main("Waiter")
			
			openoutput += "\n\n__Owner__\nName: " 
			openoutput += owner["name"] + "\nA " 
			openoutput += owner["gender"] + " "+ str(owner["age"]) + "\nCharacteristic: " + owner["characteristic"]
			openoutput += "\n\n__Waiter__\nName: " + waiter["name"] + "\nA " 
			openoutput += waiter["gender"] + " " + str(waiter["age"]) + "\nCharacteristic: " + waiter["characteristic"]
			secretoutput += "\n\n__Owner__\nName: " + owner["name"] + "\nA " 
			secretoutput += owner["gender"] + " " + str(owner["age"]) + "\nCharacteristic: " + owner["characteristic"] \
			+ "\nTrait: " + owner["trait"]
			if owner["secret"] != "Has no secret":
				secretoutput += "\nSecret: " + owner["secret"]
			secretoutput += "\n\n__Waiter__\nName: " + waiter["name"] + "\nA "
			secretoutput += waiter["gender"] + " " + str(waiter["age"]) + "\nCharacteristic: " \
			+ waiter["characteristic"]+ "\nTrait: " + waiter["trait"]
			if waiter["secret"] != "Has no secret":
				secretoutput += "\nSecret: " + waiter["secret"]
		
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
		if len(arg) == 0:
			arg.append(0)
			
		try:
			arg[0] = int(arg[0])
			if arg[0] > 5:
				openoutput = "The maximum size of a settlement is five, see itemlist for more info"
			else:			
				openoutput, secretoutput = fantasysettlementformat(fantasysettlementgenerator.main(arg[0]))
		except ValueError:
			openoutput = "The input must be a number between 1 and 5, see itemlist for more info"
				
			
		
	elif item == "fantasyoutpost" or item == "foutpost": #fantasy outpost
	
		dum = fantasysettlementgenerator.main(1)
		
		if len(arg) == 0:
			arg.append(0)

		if type(arg[0])== str:
			dum["name"] = arg[0]
			
		openoutput, secretoutput = fantasysettlementformat(dum)

	elif item == "fantasyhamlet" or item == "fhamlet": #fantasy hamlet
			
		dum = fantasysettlementgenerator.main(2)
		
		if len(arg) == 0:
			arg.append(0)

		if type(arg[0])== str:
			dum["name"] = arg[0]
			
		openoutput, secretoutput = fantasysettlementformat(dum)
		
	elif item == "fantasyvillage" or item == "fvillage": #fantasy village
			
		dum = fantasysettlementgenerator.main(3)
		
		if len(arg) == 0:
			arg.append(0)

		if type(arg[0])== str:
			dum["name"] = arg[0]
			
		openoutput, secretoutput = fantasysettlementformat(dum)
		
	elif item == "fantasytown" or item == "ftown": #fantasy town
			
		dum = fantasysettlementgenerator.main(4)
		
		if len(arg) == 0:
			arg.append(0)

		if type(arg[0])== str:
			dum["name"] = arg[0]
			
		openoutput, secretoutput = fantasysettlementformat(dum)
		
	elif item == "fantasyvcity" or item == "fcity": #fantasy city
			
		dum = fantasysettlementgenerator.main(5)
		
		if len(arg) == 0:
			arg.append(0)

		if type(arg[0])== str:
			dum["name"] = arg[0]
			
		openoutput, secretoutput = fantasysettlementformat(dum)
		
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
		
	elif item == "fantasybookcase" or item == "fbookcase" or item == "fbc": #fantasy book
		
		if len(arg) == 0:
			arg.append(4)
			
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
		argslist = ["all", "empty", "empty"]

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
	except NameError: secretoutput = openoutput
	
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
			
			for j in range(1,i
			):
				split2 = split1[j].split("]]")
				list = split2[0].split("/")
				openoutput += memory[0][memory.index(list)] + split2[1]

			
	secretoutput = secretoutput.replace("  ", " ", 10)	
	secretoutput = secretoutput.replace(" .", ".", 1)		
	secretoutput = secretoutput.replace(" ,", ",", 1)	
	openoutput = openoutput.replace("  ", " ", 10)	
	openoutput = openoutput.replace(" .", ".", 1)		
	openoutput = openoutput.replace(" ,", ",", 1)
	
	return(openoutput, secretoutput)
	

	
	
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
#					Formating functions
# /|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|//|\\|/
	
def charaformat(character):

	output = character["name"]
	dummy = str(str(character["gender"])) + " " + str(character["age"]) + " " + str(character["occupation"] + ".")
	output += "\nA " + dummy.lower()
	output += "\nCharacteristic: " + character["characteristic"]
		 
	openoutput = output
	
	output += "\nTrait: " + character["trait"] 
	
	dummy =  character["secret"]
	if str(dummy) != str("Has no secret"):
		output += "\nSecret: " + dummy
		
	secretoutput = output
	
	return(openoutput, secretoutput)
	
def secretcharaformat(character):

	output = character["name"] 
	dummy = "."
	if character["occupationgenerated"]:
		dummy = " " + str(character["occupation"]) + "."
	dummy2 = str(str(character["gender"])) + " " + str(character["age"]) + dummy
	output += "\nA " + dummy2.lower()
	output += "\nCharacteristic: " + character["characteristic"]	
	output += "\nTrait: " + character["trait"] 
	
	dummy =  character["secret"]
	if str(dummy) != str("Has no secret"):
		output += "\nSecret: " + dummy
		
	secretoutput = output
	
	return(secretoutput)
	
def fantasysettlementformat(settlement):
	
	# general settlement stuff
		
	output = "__**" + settlement["name"] + "**__\n"
	output += "Size: " + settlement["size"] + "\n"
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
	
	output = "__Ruler__\n"
	
	if settlement["ruler"]["individual"]:
		output += "Name: " + settlement["ruler"]["name"] + "\n"
		output += "A " + str(settlement["ruler"]["gender"]) + " " + str(settlement["ruler"]["age"]) + " " + str(settlement["ruler"]["occupation"]) + "\n"
		
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
		
		if institution["identifier"] == 1 or institution["identifier"] == 2: #inn/tavern
		
			output += "\nOddity: " + institution["oddity"]   \
				 + "\nSpeciality: " + institution["specialty"]				
			output += "\nSecret: " + institution["secret"]		
			
			secretoutput += output
			output = ""
			
			owner = fantasyNPCgenerator.main("Owner")
			
			secretoutput += "\n\n__Owner__\n" + secretcharaformat(owner) + "\n"
			
			# Removed Waiter from settlement inns, too much info already
			# secretoutput += "\n__Waiter__\n" + secretcharaformat(waiter) + "\n" 
		
		elif institution["identifier"] == 3: #trading post
	
			secretoutput += "\nFood vendors:\n"
			for vendor in institution["food"]:
				secretoutput += "    " + vendor + "\n"
				
			secretoutput += "Smell: " + institution["smell"] + "\n"
			
		elif institution["identifier"] == 4: #Temple
		
			secretoutput += "\nPrincipal succour: " + institution["succour"] + "\n"
			
			highpriest = fantasyNPCgenerator.main("High priest")
			
			secretoutput += "\n__High priest__\n" + secretcharaformat(highpriest) + "\n"
			
		elif institution["identifier"] == 5: #Library
		
			secretoutput += "\nAreas of focus:\n"
			for discipline in institution["disciplines"]:
				secretoutput += "    " + discipline + "\n"
				
			librarian = fantasyNPCgenerator.main("Librarian")
			
			secretoutput += "\n__Librarian__\n" + secretcharaformat(librarian) + "\n"
				
		elif institution["identifier"] == 6: #University
		
			secretoutput += "\nClasses taught:\n"
			for discipline in institution["disciplines"]:
				secretoutput += "    " + discipline + "\n"
				
			dean = fantasyNPCgenerator.main("Dean")
			
			secretoutput += "\n__Dean__\n" + secretcharaformat(dean) + "\n"
			
		elif institution["identifier"] == 7: #Park
		
			secretoutput += "\nCentre piece: " + institution["centrepiece"] + "\n"
			

			
	return(openoutput, secretoutput)