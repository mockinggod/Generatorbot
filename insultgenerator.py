import random

#The output is an object with seven keys output["name"], output["age"], output["characteristic"], output["trait"], output["occupation"], output["gender"], output["secret"]
 
with open("insultsappearance.txt", encoding='latin-1') as f:
    appearancelist = f.read().splitlines()
	
with open("insultscharacter.txt", encoding='latin-1') as f:
    characterlist = f.read().splitlines() 
	
with open("insultsintelligence.txt", encoding='latin-1') as f:
    intelligencelist = f.read().splitlines() 	
	
with open("insultsmisc.txt", encoding='latin-1') as f:
    misclist = f.read().splitlines() 	
	
with open("insultscomeback.txt", encoding='latin-1') as f:
    comebacklist = f.read().splitlines() 	
	
	
	
	
def main(type = "default", type2 = "empty", type3 = "empty", type4 = "empty"):
# Pulls an insult from four list, you can specify which list

	insultlist = {
		"appearance": appearancelist,
		"character": characterlist,
		"intelligence": intelligencelist,
		"misc": misclist,
		"comeback": comebacklist,		
		"default": appearancelist + characterlist + intelligencelist + misclist,
		"all": appearancelist + characterlist + intelligencelist + misclist + comebacklist,
		"empty": []
	}
	
	if type in insultlist:
	
		if type2 in insultlist:
		
			if type3 in insultlist:
		
				if type4 in insultlist:
			
					output = str(random.choice(insultlist[type] + insultlist[type2] + insultlist[type3] + insultlist[type4]))
					
				else:
				
					output = type4 + "is not a recognized type of insult"
				
			else:
			
				output = type3 + "is not a recognized type of insult"
			
		else:
		
			output = type2 + "is not a recognized type of insult"
		
	else:
	
		output = type + "is not a recognized type of insult"
		
	return(output)
   


   

