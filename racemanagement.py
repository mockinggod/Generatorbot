import names
import psqlfunctions as psqlf

#extract races with a given name
def exracebyn(races, race):
	output = []
	for ra in races:
		if race == ra['racename']:
			output.append(ra)

	return(output)

#extract races that can live in a given set size			
def exracebys(races, size):
	output = []
	size = int(size)
	for ra in races:
		if ra['maxsettlement'] > 0 or ra['maxsettlement'] not in range(-5+size,-10+size):
			if ra['maxsettlement'] != 0:
				output.append(ra)
	return(output)
	
def addfantasyrace(ctx, serverinfo, race, gender, weight, namesethnicity, surnamesethnicity, maxsettlement, occupations):
#allows a user to add a race to their custom lists of fantasy races


	
	if race == None:
		output = "Type @prefix@info races to learn how to use this."	
		
				
	else:
				
		if gender == None:
		
		
			output = ""
		
			
			gender = "both"
			
		elif gender == "none":
		
			gender = ""
			
			output = "genderless" 
			
			
		else:
				
			output = ""
			
		if weight is None:
			weight = 1.0
			
		try:
			float(weight)
			floatisnumber = True
		except:
			floatisnumber = False
			
		if floatisnumber and floatisnumber<1000:
						
			if namesethnicity == None:
			
				if gender == 'female':
					psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, gender, float(weight), 'engf', 'engsur', maxsettlement, occupations])
				elif gender == 'both':
					psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, "female", float(weight), 'engf', 'engsur', maxsettlement, occupations])
					psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, "male", float(weight), 'engm', 'engsur', maxsettlement, occupations])
					gender = 'both male and female'
				else:
					psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, gender, float(weight), 'engm', 'engsur', maxsettlement, occupations])
				output += gender + " " + race + " added to your personal list of races"
				
			elif surnamesethnicity == None:
			
				if namesethnicity.lower() in names.strings or (gender == 'both' and namesethnicity.lower() in names.ethnicities):
				
					if gender == 'both':
						psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, "female", float(weight), namesethnicity.lower()+"f", 'engsur', maxsettlement, occupations])
						psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, "male", float(weight), namesethnicity.lower()+"m", 'engsur', maxsettlement, occupations])
						gender = 'both male and female'
					else:
						psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, gender, float(weight), namesethnicity.lower(), 'engsur', maxsettlement, occupations])
					output += gender + " " + race + " added to your personal list of races"
				
				else:
				
					output = namesethnicity + " is not valid a names category"
				
			else:
							
				if namesethnicity.lower() in names.strings or (gender == 'both' and namesethnicity.lower() in names.ethnicities):
					if surnamesethnicity.lower() in names.strings:
					
						try: 
							int(maxsettlement)
							if int(maxsettlement) in range(-9,9):

								if occupations[0] == "[":
									occupations = occupations[1:-1]
									dumoccupatins = [""]
									i = 0
									for element in occupations:
										if element == ",":
											dumoccupatins[i] = float(dumoccupatins[i])
											i += 1
											dumoccupatins.append("")
										else:
											dumoccupatins[i] += element
									dumoccupatins[i] = float(dumoccupatins[i])
									
									occupations = dumoccupatins
										
							
								if(isinstance(occupations, list) and len(occupations) == 11):
									check = []
									
									for test in occupations:
										if isinstance(test, int) or isinstance(test, float):
											check.append(True)
										else:
											check.append(False)
											
									if all(check):
									
										if gender == 'both':
											psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, "female", float(weight), namesethnicity.lower()+"f", surnamesethnicity.lower(), maxsettlement, occupations])
											psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, "male", float(weight), namesethnicity.lower()+"m", surnamesethnicity.lower(), maxsettlement, occupations])
											gender = 'both male and female'
										else:
											psqlf.addrace(serverinfo, ctx.message.author.id, "fantasy", [race, gender, float(weight), namesethnicity.lower(), surnamesethnicity.lower(), int(maxsettlement), occupations])
										output += gender + " " + race + " added to your personal list of races"
							
									else:
										
										output = "occupations must be a list made up of 11 numbers, type @prefix@info races for more information"
										
								else:
									output = "occupation must be a list made up of 11 numbers, type @prefix@info races for more information"

							else:
								output = maxsettlement + " is not a whole number, maxsettlement must be a whole number between -9 and 9, type @prefix@info races for more information"
						except ValueError:
							output = maxsettlement + " is not a whole number, maxsettlement must be a whole number between -9 and 9, type @prefix@info races for more information"
							
					else:
						output = surnamesethnicity + " is not valid a surnames category, type @prefix@info ethnicities for more information"
						
				else:
					output = namesethnicity + " is not valid a names category, type @prefix@info ethnicities for more information"
					
		else:
			output = weight + " is not a number, weight must be a number, type @prefix@info races for more information"
			
	return(str(output))
					
			