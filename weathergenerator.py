import numpy as np
import homebrew as hb

# import the content from the text files
templist = (hb.arrayreader("temperatures.txt"))
weatherlist = (hb.arrayreader("weathers.txt"))
rareweatherlist = (hb.arrayreader("rareweathers.txt"))

def main(input):

	rand = np.random.random()
	
	#initialize lists
	templistselect = []
	templistselect2 = []
	weatherlistselect = []
	weatherlistselect2 = []
	
	#sets a random but weighted temperature for the provided climate, temp takes values between 1 and 5
	
	if(input=="arctic" or input=="polar" or input=="1"):
	
		if rand < 0.6:
			temp = 1
		elif rand < 0.97:
			temp = 2
		else:
			temp = 3
			
	elif(input=="winter" or input=="cold"or input=="2" ):
	
		if rand < 0.25:
			temp = 1
		elif rand < 0.75:
			temp = 2
		elif rand < 0.99:
			temp = 3
		else:
			temp = 4
			
	elif(input=="summer" or input=="hot" or input=="4"):
	
		if rand < 0.01:
			temp = 2
		elif rand < 0.25:
			temp = 3
		elif rand < 0.25:
			temp = 4
		else:
			temp = 5
			
	elif(input=="desert" or input=="drought" or input=="5"):

		if rand < 0.03:
			temp = 3
		elif rand < 0.4:
			temp = 4
		else:
			temp = 5
			
	elif(input=="chaos" or input=="random" or input=="r"):
		
		if rand < 0.2:
			temp = 1
		elif rand < 0.4:
			temp = 2
		elif rand < 0.6:
			temp = 3
		elif rand < 0.8:
			temp = 4
		else:
			temp = 5

	else:
	
		if rand < 0.02:
			temp = 1
		elif rand < 0.25:
			temp = 2
		elif rand < 0.75:
			temp = 3
		elif rand < 0.98:
			temp = 4
		else:
			temp = 5
			
	#pom stand for plus or minus, if there is a second set of temp and weather, this determinism if it is colder or hot then the first.
	if temp == 1:
		pom = 1
	elif temp == 5:
		pom = -1
	else:
		pom = np.random.choice([-1,1])
	
	#creates a list of all the temperature descriptions that match the value temp
	for t in templist:
		if(int(t[0]) == temp):
			templistselect.append(t[1])
			
	#creates a list of all the temperature descriptions that match the value temp plus or minus 1			
		if(int(t[0]) - temp == pom):
			templistselect2.append(t[1])	
			
				
	rand = np.random.random()
	if rand<0.002: #very rare but epic weather: eruptions, eclipses...
		formats = []
		#The replace function need the following lists to be none empty enven if they are not being used.
		weatherlistselect = ["This should not be visible"]
		weatherlistselect2 = ["This should not be visible"]
		for weather in rareweatherlist:
			if(int(weather[0]) == temp or int(weather[0]) == 0):
				formats.append(weather[1])	

				
		output = np.random.choice(formats)
		
		
	else: #normal weather
		for weather in weatherlist:
			#creates a list of all the weather descriptions that match the value temp or weathers that occur at all temperatures 
			if(int(weather[0]) == temp or int(weather[0]) == 0):
				weatherlistselect.append(weather[1])
				
			#creates a list of all the weather descriptions that match the value temp pom 1, doesn't to include weathers that occur at all temperatures to make repetitions impossible
			if(int(weather[0]) - temp == pom):
				weatherlistselect2.append(weather[1])


		# The possible formats that the weather statements can come in, I repeated my favorite as a crude way or weighting them
		formats = ["It's @temperature@ and @weather@.",\
			"The temperature is @temperature@ and @its@@weather@.",\
			"It's @temperature@ and @weather@.",\
			"The air is @temperature@ and @its@@weather@.",\
			"It's a @temperature@ day and @and1@@its@@weather@@and2@",\
			"It's a @temperature@ day and @and1@@its@@weather@@and2@",\
			"The [[air/ temperature]] goes from @temperature@ to @temperature2@ and it's @weather@.",\
			"In the mourning it's @temperature@ and @weather@ in the afternoon it's @temperature2@ and @weather2@.",\
			"The mourning is @temperature@ and @weather@, the afternoon is @temperature2@ and @weather2@."\
			]

		output = np.random.choice(formats)
	
	# Applies the numerous changes needed to make the sentence from different formats make grammatical sense 
	output = output.replace("@temperature@", str(np.random.choice(templistselect)), 1)
	output = output.replace("@temperature2@", str(np.random.choice(templistselect2)), 1)
	output = output.replace("@weather@", str(np.random.choice(weatherlistselect)), 1)	
	output = output.replace("@weather2@", str(np.random.choice(weatherlistselect2)), 1)
	output = output.replace("day and @and1@@its@@its@@and1@", "and ", 4)
	output = output.replace("@its@@its@", "it's", 4)	
	output = output.replace("@its@", "", 4)	
	output = output.replace("day and @and1@@and1@", "and ", 4)	
	output = output.replace("@and1@", "", 4)	
	output = output.replace("@and2@@and2@", "day", 4)	
	output = output.replace("@and2@", "", 4)	
	output = output.replace("day and it's@and1@", "and ", 1)		
	output = output.replace("it's @itseater@", "", 4)
	output = output.replace("@itseater@", "", 4)
	output = output.replace("  ", " ", 10)	
	output = output.replace(" .", ".", 1)		

	return(output)
