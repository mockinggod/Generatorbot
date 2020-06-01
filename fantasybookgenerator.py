import numpy as np
import randomnamegenerator

	
with open("malename.txt", encoding='latin-1') as f:
    firstname = f.read().splitlines() 
	
with open("femalename.txt", encoding='latin-1') as f:
    firstname += f.read().splitlines() 
	
with open("medievalmalename.txt", encoding='latin-1') as f:
    firstname += f.read().splitlines() 
	
with open("medievalfemalename.txt", encoding='latin-1') as f:
    firstname += f.read().splitlines() 
	
with open("surname.txt", encoding='latin-1') as f:
    surname = f.read().splitlines() 
	
with open("medievalsurname.txt", encoding='latin-1') as f:
    surname += f.read().splitlines() 
	


def main():

	with open("booksecret.txt", encoding='latin-1') as f:
		secret = f.read().splitlines() 
		
	with open("fantasybooksecret.txt", encoding='latin-1') as f:
		secret += f.read().splitlines() 

	namingscheme = ["@start@ @adjective@ @booktype@ @subject@",\
		"@start@ @booktype@ @subject@",\
		"@start@ @adjective@ @subject@",\
		"@booktype@ @subject@",\
		"@adjective@ @booktype@ @subject@",\
		"@adjective@ @subject@",\
		"@start@ @subject@",\
		"@start@ @booktype@ @subject@",\
		"@start@ @adjective@ @subject@",\
		"@booktype@ @subject@",\
		"@adjective@ @subject@",\
		"@start@ @subject@",\
		"@subject@"]

	start = ["@authorfullname@'s", "@authorsurname@'s", "@surname@'s", "The"]
	
	adjective = ["Awesome", "Ultimate", "Final", "Magnificent", "Great", "Practical"]
	
	subjects = ["should never appear", "neither should this"]
	
	booktype = ["Study of", "Study in", "Guide to", "Tutorial in", "Encyclopedia of", "Introduction to",\
		"Manual of", "Essay on", "Book on", "Book of", "Musing on", "Introduction on"]
		
		
	state = ["Brand new",\
		"Like new",\
		"Very good",\
		"Good",\
		"Decent",\
		"Worn",\
		"Damaged",\
		"Aged",\
		"Dusty",\
		"Ancient",\
		"Missing a few pages",\
		"Missing the front cover",\
		"Chard edges",\
		"Smudged ink",\
		"Crinkled pages",\
		"Missing most pages",\
		"Most pages fall to dust as you open it",\
		"Pages glued and cut to stash a bottle"\
		]

		
		
	part1 = ["Should never shown"]
	part2 = ["Should never shown"]
		
	selector = np.random.random()*10.2

	
	output = {}
	
	if selector < 1: #Fiction
		output["subject"] = "fiction"
		
		subselector = np.random.random()*10
		
		with open("fictionbooknamepart1.txt", encoding='latin-1') as f:
			part1 = f.read().splitlines() 
 
		with open("fictionbooknamepart2.txt", encoding='latin-1') as f:
			part2 = f.read().splitlines() 
		
		namingscheme = ["the @part1@ @part2@", "the @part2@ and the @part2@", "@part2@ and @part2@", \
			"The @part2@", "@fullname@", "@firstname@ and @firstname@"]
			
		authorjob = ["Writer", "Novelist", "Scribe", "Amateur"]
		
		focus = ["Character", "Story", "Motivation", "Consequences", "Philosophy", "Emotion"]
		
		secret.extend(["The story is based on real secret events"])
		
		if subselector < 1:
			output["branch"] = "romance"
			
			part1.extend(["Loving", "Shy", "Lonely", "Handsome"])
			part2.extend(["Lover", "Prince", "Princess", "Bachelor", "Widow", "Maiden", "Nurse", "Kiss"])
			
			authorjob.extend(["house wife", "courtesan"])
			
			focus.extend(["romance", "relationship"])
			
		elif subselector < 2:
			output["branch"] = "adventure"
			
			part1.extend(["Mighty", "Wandering", "Deadly"])
			part2.extend(["Fool", "Bow", "Blade", "Pirate", "Thief", "Wizard", "Mage", "Killer", "Healer"])
			
			authorjob.extend(["veteran", "ex adventure"])
			
			focus.extend(["combat", "violence", "morality", "exploration", "friendship"])
			
		elif subselector < 3:
			output["branch"] = "epic"
			
			part1.extend(["Mighty", "Wandering", "Deadly", "Godly", "Awesome", "Ultimate", "First"])
			part2.extend(["Titan", "God", "World", "Wizard", "Killer", "Savior"])
			
			authorjob.extend(["ex adventure", "philosopher"])
			
			focus.extend(["combat", "violence", "morality"])
			
		elif subselector < 4:
			output["branch"] = "mystery"
			
			part1.extend(["Poison", "Shadow", "Deadly", "Last"])
			part2.extend(["Mist", "Poison", "World", "Enigma", "Killer", "Mystery", "Body", "Cult", "Case"])
			
			authorjob.extend(["house wife", "detective", "philosopher"])
			
			focus.extend(["investigation", "psychology", "morality"])
			
		elif subselector < 5:
			output["branch"] = "fairy tale"
			
			part1.extend(["Poison", "Shadow", "Candy", "Last", "Honey", "Happy", "Little", "Wonderful"])
			part2.extend(["Bunny", "Witch", "World", "Wolf", "Biscuit", "Mystery", "Puppy"])
			
			authorjob.extend(["house wife", "teacher", "philosopher"])
			
			focus.extend(["education", "psychology", "morality"])
			
		elif subselector < 6:
			output["branch"] = "short stories"
			
			namingscheme = ["the @part1@ @part2@", \
				"The @part2@", "@authorfullname@'s @part2@", "@authorsurname@'s @part2@"]
			
			part2 = ["Compilation", "Collection", "Anthology", "Book", "Story"]
			
			authorjob.extend(["different authors", "philosopher", "scholar"])
			
			focus.extend(["society", "humanity", "morality"])
			
		elif subselector < 7:
			output["branch"] = "science fiction"
			
			part1.extend(["Futur", "Science", "Potential", "Predictive", "Time", "New"])
			part2.extend(["Machine", "Sun", "Human", "Galaxy", "Moon"])
			
			authorjob.extend(["scientist", "philosopher", "scholar"])
			
			focus.extend(["society", "humanity", "morality", "science", "perspective"])
			
		elif subselector < 8:
			output["branch"] = "horror"
			
			part1.extend(["Poison", "Shadow", "Wrong", "Last", "Fearful", "Unending", "Strange"])
			part2.extend(["Monster", "Abomination", "Sleep", "Vampire", "Sacrifice"])
			
			authorjob.extend(["mental patient", "philosopher"])
			
			focus.extend(["society", "psychology", "morality", "religion"])
			
		elif subselector < 9:
			output["branch"] = "drama"
			
			
			part1.extend(["Waiting", "Critical", "Wrong", "Strange"])
			part2.extend(["Community", "Affair", "Town", "Syndicate", "Hope"])
			
			authorjob.extend(["house wife", "courtesan"])
			
			focus.extend(["society", "psychology", "morality", "relationship"])
			
		else:
			output["branch"] = "erotica"
			
			part1.extend(["Loving", "Shy", "Lonely", "Handsome", "Ardent", "Sexy", "Busty"])
			part2.extend(["Lover", "Prince", "Princess", "Bachelor", "Widow", "Maiden", "Nurse", "Harlot"])
			
			authorjob.extend(["house wife", "courtesan"])
			
			focus = ["romance", "relationship", "taboo", "decadence"]
		
	elif selector < 2: #Recipes
		output["subject"] = "Recipes"
		
		subselector = np.random.random()*10
		
		namingscheme = ["@start@ @adjective@ @subject@",\
			"@start@ @subject@",\
			"@adjective@ @subject@",\
			"@subject@"]
		
		subjects = ["Cookbook", "Recipes"]
			
		authorjob = ["Cook", "Critique", "Amateur"]
		
		adjective.extend(["Delicious", "Wonderful", "Hearty", "Tasty"])
		
		secret.extend(["Some of the recipes are for magical concoctions",\
			"The writer is a imposter with no knowledge of cooking"])
		
		if subselector < 1:
			output["branch"] = "starters"
			
			subjects.extend(["Salads", "Starters", "Amuse Bouches", "Appetiser", "Hors d'Oeuvre"])
			
			focus = ["Freshness", "Consistency", "Crispness", "Health", "Flavour", "Presentation", "Speed"]
			
		elif subselector < 2:
			output["branch"] = "main course"
			
			subjects.extend(["Dishes"])
			
			focus = ["Consistency", "Health", "Flavour", "Presentation", "Speed"]
			
		elif subselector < 3:
			output["branch"] = "desert"
			
			subjects.extend(["Deserts", "Pudding", "Afters", "Sweets", "Cakes"])
			
			focus = ["Consistency", "Health", "Flavour", "Presentation", "Speed"]
			
		elif subselector < 4:
			output["branch"] = "roast"
			
			subjects.extend(["Roasts"])
			
			focus = ["Health", "Flavour", "Presentation", "Moistness", "Timing"]
			
		elif subselector < 5:
			output["branch"] = "simple"
			
			subjects.extend(["Marvels", "Wonders", "Surprises"])
			
			focus = [ "Consistency", "Health", "Flavour", "Speed", "Price"]
			
		elif subselector < 6:
			output["branch"] = "traditional"
			
			subjects.extend(["Cuisine"])
			
			focus = ["Consistency", "Health", "Flavour", "Presentation", "Authenticity"]
			
		elif subselector < 7:
			output["branch"] = "experimental"
			
			subjects.extend(["Marvels", "Wonders", "Surprises"])
			
			focus = [ "Consistency", "Health", "Flavour", "Presentation", "Uniqueness"]
			
		elif subselector < 8:
			output["branch"] = "baking"
			
			subjects.extend(["Bakes", "Pies", "Tarts", "Biscuits", "Bread", "Viennoiserie"])
			
			focus = [ "Crust", "Health", "Flavour", "Presentation", "Speed", "Moistness"]
			
		elif subselector < 9:
			output["branch"] = "sauces"
			
			subjects.extend(["Sauces", "Dressings", "Condiments", "Jus", "Gravy"])
			
			focus = [ "Flavour", "Presentation", "Speed", "Consistency"]
			
		else:
			output["branch"] = "brewing"
			
			subjects = ["Brews", "Casks", "Recipes", "Beer"]
			
			focus = [ "Head", "Filtering", "Body", "Hops", "Flavour", "Fermentation"]
		
	elif selector < 3: #Art
		output["subject"] = "art"
		
		subselector = np.random.random()*10
		
		subjects = ["the Art"]
			
		authorjob = ["Artist", "Critique", "Amateur"]
		
		focus = ["History", "Culture", "Philosophy", "Emotion"]
		
		adjective.extend(["Tasteful", "Wonderful", "Heart felt", "Delightful", "Exquisite"])
		
		secret.extend(["The writer is a imposter with no knowledge of art"])
		
		if subselector < 1:
			output["branch"] = "theatre"
			
			subjects.extend(["Theatre", "Plays", "Drama", "Comedy"])
			
			focus = ["Acting", "Writing", "Pacing", "Oganisation", "Character", "Dialog", "Scenery"]
			
			adjective.extend(["Entertaining", "Captivating", "Riveting"])
			
		elif subselector < 2:
			output["branch"] = "poetry"
			
			subjects.extend(["Poetry", "Limericks", "Odes", "Haikys", "Couplets", "Free Verse", "Sonnets", "Dimeter"])
			
			focus = ["Rythming", "Rythem", "Imagery", "Alexandrine", "Ambiguity", "Dialog", "Stylistic device"]
			
			adjective.extend(["Melodious", "Marvelous", "Pleasant"])
			
		elif subselector < 3:
			output["branch"] = "music"
			
			subjects.extend(["Concerto", "Symphony", "Music", "Harmonics", "Melody"])
			
			focus = ["Measure", "Beat", "Ensemble", "Form", "Harmony", "Dialog", "Motif", "Tempo", "Theme"]
			
			adjective.extend(["Melodious", "Harmonious", "Soothing"])
			
		elif subselector < 4:
			output["branch"] = "songs"
			
			subjects.extend(["Songs", "Melody", "Balade", "Sonnets", "Chants", "Chorus"])
			
			focus = ["Measure", "Beat", "Ensemble", "Harmony", "Dialog", "Motif", "Theme", "Message", "Stylistic device"]
			
			adjective.extend(["Melodious", "Harmonious", "Soothing", "Captivating", "Riveting"])
			
		elif subselector < 5:
			output["branch"] = "architecture"
			
			subjects.extend(["Architecture", "Buildings", "Design", "Forms", "Planning"])
			
			focus = ["Proportions", "Functionality", "Arches", "Organisation", "Lighting",\
				"Motif", "Theme", "Symmetry", "Facade", "Materials", "Structural load"]
				
			adjective.extend(["Elegant", "Harmonious", "Beautiful", "Aesthetic"])
			
		elif subselector < 6:
			output["branch"] = "sculpture"
			
			subjects.extend(["Sculpture", "Statues", "Engraving", "Forms"])
			
			focus = ["Proportions", "Details", "Motif", "Theme", "Movement", "Symmetry", "Materials", "Structural load"]
			
			adjective.extend(["Elegant", "Harmonious", "Beautiful", "Graceful", "Aesthetic"])
			
		elif subselector < 7:
			output["branch"] = "painting"
			
			subjects.extend(["Painting", "Oil Painting", "Watercolour", "Mural"])
			
			focus = ["Proportions", "Details", "Motif", "Theme", "Movement", "Paints", "Brushes", "Technique", "Symbolism"]
			
			adjective.extend(["Elegant", "Colourful", "Beautiful", "Graceful", "Aesthetic"])
			
		elif subselector < 8:
			output["branch"] = "fashion"
			
			subjects.extend(["Fashion", "Tailoring", "Jewelery", "Hairdressing", "Attire", "Apparel"])
			
			focus = ["Proportions", "Details", "Motif", "Theme", "Movement", "Materials", "Technique", "Dimensionality"]
			
			adjective.extend(["Elegant", "Colourful", "Beautiful", "Graceful", "Aesthetic"])
			
		elif subselector < 9:
			output["branch"] = "drawing"
			
			subjects.extend(["Drawing", "Sketching", "Portrayal"])
			
			focus = ["Proportions", "Details", "Motif", "Movement", "Speed", "Accuracy", "Technique"]
			
			adjective.extend(["Elegant", "Accurate", "Beautiful", "Graceful", "Aesthetic"])
			
		else:
			output["branch"] = "ceramic"
			
			subjects.extend(["Ceramics", "Vases", "Bols", "Poetry"])
			
			focus = ["Proportions", "Details", "Motif", "Uniformity", "Speed", "Symmetry", "Technique"]
			
			adjective.extend(["Elegant", "Colourful", "Beautiful", "Graceful", "Aesthetic"])
		
	elif selector < 4: #Combat
		output["subject"] = "combat"
		
		subselector = np.random.random()*10
		
		subjects = ["Combat", "Battle", "Conflict"]
			
		authorjob = ["Soldier", "Veteran", "Historian", "Mercenary"]
		
		focus = ["History", "Training", "Discipline", "Recent Development"]
		
		adjective.extend(["Advanced", "Modern", "Real", "Reliable", "Dynamic", "Effective"])
		
		secret.extend(["The writer is a imposter with no knowledge of combat"])
		
		if subselector < 1:
			output["branch"] = "fencing"
			
			subjects.extend(["Fencing", "Swordplay", "Swordsmanship", "Sparing"])
			
			focus = ["Footing", "Strokes", "Rhythm", "Tactiques", "Focus", "Prediction", "Development"]
			
			adjective.extend(["Elegant", "Rapid", "Balanced", "Masterful"])
			
			authorjob.extend(["Quartermaster", "Noble"])
			
		elif subselector < 2:
			output["branch"] = "boxing"
			
			subjects.extend(["Boxing", "Pugilism", "Fisticuffs", "Sparing"])
			
			focus = ["Footing", "Blows", "Rhythm", "Tactiques", "Focus", "Prediction", "Development"]
			
			adjective.extend(["Balanced", "Masterful", "Vigorous"])
			
			authorjob.extend(["Pugilist"])
			
		elif subselector < 3:
			output["branch"] = "martial arts"
			
			subjects.extend(["Martial Art", "Art", "Sparing"])
			
			focus = ["Footing", "Blows", "Rythem", "Tactiques", "Focus", "Prediction", "Development"]
			
			adjective.extend(["Blanced", "Masterful", "Elegant", "Captivating"])
			
			authorjob.extend(["Monk", "Assassin"])
			
		elif subselector < 4:
			output["branch"] = "tactiques"
			
			subjects.extend(["Tactiques", "Planing", "Rules of the Game", "Manoeuvres"])
			
			focus = ["Terain", "Moral", "Communication", "Formations", "Analysis"]
			
			adjective.extend(["Potent", "Balanced", "Elegant", "Dynamic"])
			
			authorjob.extend(["Captain", "Sergeant"])
			
		elif subselector < 5:
			output["branch"] = "strategy"
			
			subjects.extend(["Strategy", "Planing", "Rules of the Game", "Military Science", "Art of War"])
			
			focus = ["Terrain", "Moral", "Communication", "Equipment", "Logistics", "Recruitment", "Analysis"]
			
			adjective.extend(["Balanced", "Masterful", "Elegant", "Dynamic"])
			
			authorjob.extend(["Noble", "General"])
			
		elif subselector < 6:
			output["branch"] = "leadership"
			
			subjects.extend(["Leadership", "Authority"])
			
			focus = ["Connection", "Respect", "Communication", "Management", "Loyalty", "Recruitment", "Analysis", "Discipline"]
			
			adjective.extend(["Balanced", "Masterful", "Elegant", "Dynamic"])
			
			authorjob.extend(["Noble", "General"])
			
		elif subselector < 7:
			output["branch"] = "archery"
			
			subjects.extend(["Archery", "Bowmen", "Marksmanship", "Shooting"])
			
			focus = ["Strategy", "Accuracy", "Training", "Equipment"]
			
			adjective.extend(["Masterful", "Elegant", "Dynamic", "Accurate"])
			
			authorjob.extend(["Hunter"])
			
		elif subselector < 8:
			output["branch"] = "training"
			
			subjects.extend(["Training", "Drilling"])
			
			focus = ["Coordination", "Moral", "Communication", "Formations", "Analysis", "Combat", "Discipline"]
			
			adjective.extend(["Effective", "Balanced", "Dynamic"])
			
			authorjob.extend(["Captain", "Sergeant", "General"])
			
		elif subselector < 9:
			output["branch"] = "naval"
			
			subjects = ["Naval Warfare", "Naval Combat", "Naval Battles"]
			
			focus = ["Coordination", "Moral", "Communication", "Formations", "Equipment", "Combat", "Discipline", "Logistics"]
			
			adjective = ["Effective", "Balanced", "Dynamic", "Potent"]
			
			authorjob = ["Captain", "Sailor", "First Officer", "Admiral"]
			
		else:
			output["branch"] = "weaponry"
			
			subjects.extend(["Weapons", "Arsenal"])
			
			focus = ["Quality", "Tactics", "Swords", "Bows", "Spears", "Maintenance"]
			
			adjective.extend(["Effective", "Balanced", "Deadly", "Quality"])
			
			authorjob.extend(["Smith"])
		
	elif selector < 5: #History
		output["subject"] = "history"
		
		subselector = np.random.random()*8
		
		subjects = ["History"]
		
		booktype.extend(["Annals of", "Chronicles of", "Records of"])
			
		authorjob = ["Historian", "Scolar", "Seer"]
		
		focus = ["Transition", "Comparison", "Broad view", "Recent Discovery"]
		
		adjective.extend(["True", "Veridict", "Real", "Reliable", "Actual"])
		
		secret.extend(["The writer is a imposter with no knowledge of history",\
			"This book comes from a parallel world, while most information is incorrect there some interesting revelations"])
		

			
		if subselector < 1:
			output["branch"] = "recent"
			
			subjects.extend(["Today", "This Time", "Current Events", "Present-day", "Modern History"])
			
			focus.extend(["Validity", "Compilation", "Analysis", "Predictions", "Magic"])
			
			adjective.extend(["Current", "Latests", "Ongoing"])
			
		elif subselector < 2:
			output["branch"] = "anciant"
			
			subjects.extend(["Yesteryear"])
			
			focus.extend(["Validity", "Compilation", "Analysis", "Magic"])
			
			adjective.extend(["Astounding"])
			
		if subselector < 3:
			output["branch"] = "antique"
			
			subjects.extend(["Sagas", "Legends", "Myths", "Antiquity"])
			
			focus.extend(["Validity", "Compilation", "Analysis", "Magic"])
			
			adjective.extend(["Epic", "Astounding"])
			
		elif subselector < 4:
			output["branch"] = "historical figure"
			
			subjects = ["@surname@", "@fullname@"]
			
			authorjob.extend(["Relative"])
			
			focus.extend(["Early life", "Decisions", "Morals", "Success", "Failures", "Legacy"])
			
			adjective.extend(["Personal", "Astounding", "Biographical"])
			
		elif subselector < 5:
			output["branch"] = "scientific"
			
			subjects = ["Scientific History", "Scientific Advancement", "Scientific Discovery", "History of Progress"]
			
			authorjob.extend(["Scientist"])
			
			focus.extend(["Physics", "Biology", "Chemistry", "Engineering", "Math", "Humanities", "Magic"])
			
			adjective.extend(["Personal", "Astounding", "Biographical"]) 
			
		elif subselector < 6:
			output["branch"] = "political"
			
			subjects = ["Political History", "Diplomatic History", "Civic History", "Bureaucratic History"]
			
			authorjob.extend(["Politician"])
			
			focus.extend(["Morals", "Success", "Failures", "Consequences", "Popularity", "Stability"])
			
			adjective = ["Personal", "Human"]
			
			
		elif subselector < 7:
			output["branch"] = "natural"
			
			subjects = ["History of the World", "Natural History", "History of Geography", "Geological History", "Biological History", "History of life"]
			
			authorjob.extend(["Naturalist", "Druid"])
			
			focus.extend(["Recent development", "Evolution", "Early earth", "Consequences", "Environment", "The last extinction period"])
			
		else:
			output["branch"] = "economic"
			
			subjects = ["History of Money", "Financial History", "History of Financies", "Economical History"]
			
			authorjob.extend(["Economist", "Financier"])
			
			focus.extend(["Morals", "Success", "Failures", "Consequences", "Recent development"])
		
	elif selector < 6: #Geography
		output["subject"] = "geography"
		
		subselector = np.random.random()*3
		
		subjects = ["Geography", "Cartography", "Maps", "Survey"]
			
		authorjob = ["Geographer", "Cartographer", "Seer", "Scholar"]
		
		focus = ["Comparison", "Broad view", "Recent Discovery"]
		
		adjective.extend(["Reliable", "Precise", "Reliable", "Actual"])
		
		secret.extend(["The writer is a imposter with no knowledge of geography",\
			"There is secret location that can only be reached using this book"])
		
		if subselector < 1:
			output["branch"] = "local"
			
			subjects.extend(["Topography"])
			
			focus.extend(["Towns and roads", "Physical layout", "Hunting spots", "Trade goods", "Cave network", "Ore deposits",\
				"Demographics", "Lakes and Rivers", "Religion", "Politics", "Ecosystem", "Economics"])
				
			authorjob.extend(["Shepard"])
			
			booktype = ["Local", "Regional"]
			
		elif subselector < 2:
			output["branch"] = "distant"
			
			subjects.extend(["Topography"])
			
			
			focus.extend(["Towns and roads", "Physical layout", "Trade goods", "Cave network", "Ore deposits",\
				"Demographics", "Lakes and Rivers", "Religion", "Politics", "Ecosystem", "Economics"])
			
			booktype = ["Distant", "Foreign", "Faraway"]
			
		else:
			output["branch"] = "wordwide"
			
			subjects.extend(["Topography", "Atlas"])
			
			focus.extend(["Towns and roads", "Physical layout", "Trade goods", "Cave networks", "Ore deposits",\
				"Demographics", "Lakes and Rivers", "Religion", "Politics", "Culture", "Ecosystem", "Economics"])
			
			booktype = ["Worldwide", "World", "Global"]
				
	elif selector < 7: #Science
		output["subject"] = "science"
		
		subselector = np.random.random()*10

		subjects = ["Science"]
			
		authorjob = ["Scientist", "Scholar"]
		
		focus = ["History", "Teaching", "Research", "Recent Development"]
		
		adjective.extend(["Advanced", "Modern", "Real", "Reliable", "Dynamic", "Effective", "Revolutionary"])
		
		secret.extend(["The writer is a imposter with no knowledge of science"])
		
		if subselector < 1:
			output["branch"] = "mathematics"
			
			subjects = ["Mathematics", "Math", "Numbers"]
			
			authorjob.extend(["Mathematician"])
			
			focus.extend(["Algebra", "Geometry", "Trigonometry", "Statistics", "Graphing", "Number theory"])
			
			adjective.extend(["Beautiful", "Elegant"])
			
		elif subselector < 2:
			output["branch"] = "physics"
			
			subjects = ["Physics", "Mechanics", "Natural Science"]
			
			authorjob.extend(["Physicist"])
			
			focus.extend(["Mechanics", "Electromagnetic waves", "Waves", "Kinematics" "Thermodynamics"])
			
			adjective.extend(["Beautiful", "Elegant"])
			
		elif subselector < 3:
			output["branch"] = "chemistry"
			
			subjects = ["Chemistry", "Reactions", "Natural Science"]
			
			authorjob.extend(["Chemist"])
			
			focus.extend(["Acids", "Explosives", "Glues", "Lubricant", "Cleaners", "Smells"])
			
			
		elif subselector < 4:
			output["branch"] = "biology"
			
			subjects = ["Biology", "Life", "Natural Science"]
			
			authorjob.extend(["Biologist"])
			
			focus.extend(["Organs", "Tissues", "Disease", "Muscles", "Adaptation", "Habitat", "Eco-system", "Reproduction"])
			
			adjective.extend(["Beautiful", "Elegant"])
			
		elif subselector < 5:
			output["branch"] = "logic"
			
			subjects = ["Logic", "Arguments", "Rationale"]
			
			authorjob.extend(["Mathematician", "Philosopher"])
			
			focus.extend(["Mathematical", "Syllogistic", "Semantics", "Formal"])
			
			adjective.extend(["Beautiful", "Elegant"])
			
		elif subselector < 6:
			output["branch"] = "astronomy"
			
			subjects = ["Astronomy", "the Sky", "Stargazing"]
			
			authorjob.extend(["Astronomers"])
			
			focus.extend(["Time keeping", "Constellations", "Galaxies", "Planets", "Coloration"])
			
			adjective.extend(["Beautiful", "Elegant", "Endless"])
			
		elif subselector < 7:
			output["branch"] = "zoology"
			
			subjects = ["Zoology", "Life", "Bestiary"]
			
			authorjob.extend(["Zoologist", "Biologist", "Druid", "Ranger"])
			
			focus.extend(["Insects", "Mammals", "Birds", "Reptiles", "Fish", "Exotic"])
			
			adjective.extend(["Complete", "Glorious", "Endless"])
			
		elif subselector < 8:
			output["branch"] = "medicine"
			
			subjects = ["Medicine", "Life", "Healing"]
			
			authorjob.extend(["Doctor", "Biologist", "Druid", "Cleric"])
			
			focus.extend(["Animals", "Injuries", "Herbs", "Diseases", "Infection", "Surgery"])
			
			adjective.extend(["Saving"])
			
		elif subselector < 9:
			output["branch"] = "geology"
			
			subjects = ["Geology", "Earth"]
			
			authorjob.extend(["Geologist", "Druid"])
			
			focus.extend(["Mountains", "Rivers", "Lakes", "Volcanoes", "Oceans"])
			
			adjective.extend(["Timeless", "Gigantic", "Titanic"])
			
		else:
			output["branch"] = "engineering"
			
			subjects = ["Engineering", "Design"]
			
			authorjob.extend(["Engineer", "Inventor"])
			
			focus.extend(["Construction", "Clockwork", "Mechanics", "Electrical", "Magnetism", "Weaponry"])
			
			adjective.extend(["Revolutionary", "Mighty", "Robust"])
		
	elif selector < 8: #Religion
		output["subject"] = "religion"
		
		subselector = np.random.random()*10
		
		authorjob = ["Cleric", "Scribe"]
		
		secret.extend(["The writer is a imposter with no knowledge of theology"])
			
		if subselector < 3:
			output["branch"] = "holy book"
			
			part1 = ["Holy", "Divine", "Sacred", "Blessed", "Good", "Hallowed", "Consecrated", "Heavenly", "Mighty"]
			
			part2 = ["Book", "Laws", "Teachings", "Text", "Master", "God",\
				"Gospel", "Song", "Doctrine", "Records", "Tome"]
			
			namingscheme = ["the @part1@ @part2@","the @part1@ @part2@", "The @part2@", "the @part1@ @random@", "The @random@"]
			
			authorjob.extend(["Prophet", "God"])
		
			focus = ["Morals", "Philosophy", "Laws", "History", "Rites"]
			
		elif subselector < 5:
			output["branch"] = "prayer book"
			
			subjects = ["Prayers", "Hymns"]
			
			focus = ["Morals", "Philosophy", "Laws", "History"]
			
			adjective = ["Holy", "Divine", "Sacred", "Blessed", "Hallowed", "Consecrated", "Heavenly", "Mighty"]			
			
		elif subselector < 6:
			output["branch"] = "rituals"
			
			subjects = ["Rituals", "Rites", "Ceremonies", "Sacrament", "Customs", "Traditions"]
			
			focus = ["Morals", "Philosophy", "Laws", "History"]
			
			adjective = ["Holy", "Divine", "Sacred", "Blessed", "Hallowed", "Consecrated", "Heavenly", "Mighty"]
			
		elif subselector < 7:
			output["branch"] = "book of saints"
			
			subjects = ["Saints", "the Martyrs", "Prophets", "Paragons"]
			
			focus = ["Morals", "Philosophy", "Laws", "History"]
			
			adjective = ["Holy", "Divine", "Sacred", "Blessed", "Hallowed", "Consecrated", "Heavenly"]
			
		elif subselector < 9:
			output["branch"] = "propaganda"
			
			subjects = ["Truths", "Truth", "Awakening", "Absolution", "Mercy", "Delivery"\
				, "Liberation", "Rebirth", "Salvation"]
			
			focus = ["Morals", "Philosophy", "Heaven", "History", "Successes"]
			
			authorjob.extend(["Preacher", "Missionary"])
			
			adjective = ["Holy", "Divine", "Sacred", "Blessed", "Hallowed", "Consecrated", "Heavenly"]
			
		else:
			output["branch"] = "prophecies"
			
			subjects = ["Truths", "the Truth", "Awakening", "Absolution", "Mercy", "Delivery"\
				, "Liberation", "Rebirth"]
			
			focus = ["Decisions", "Moral", "Judgment", "End Times", "Rapture"]
			
			adjective = ["Holy", "Divine", "Sacred", "Blessed", "Hallowed", "Consecrated", "Heavenly"]
		
	elif selector < 9: #Magic
		output["subject"] = "magic"
		
		subselector = np.random.random()*12
			
		authorjob = ["Mage", "Archmage", "Wizard", "Sorcerer"]
		
		focus = ["Initiation", "Speed", "Power", "Recent Development", "Control", "Theory", "Efficiency"]
		
		adjective.extend(["Advanced", "Modern", "Controlled", "Powerful", "Dynamic", "Effective", "Revolutionary", "Arcane"])
		
		booktype.extend(["Spellbook of", "Grimoire of", "Scrolls of", "Codex of"])
		
		secret.extend(["The writer is a imposter with no knowledge of magic",\
		"The book contains spells that anyone can cast by reading them",\
		"Some of the spells are traps layed out by the writer"])
		
		if subselector < 1:
			output["branch"] = "evocation"
			
			subjects = ["Evocation", "Destruction"]
			
			authorjob.extend(["Battle Mage", "Elementalist"])
			
			focus.extend(["Fire", "Frost", "Lighting", "Psychic", "Impact", "Cuts"])
			
			adjective.extend(["Deadly", "Lethal", "Terrifying"])
			
		elif subselector < 2:
			output["branch"] = "divination"
			
			subjects = ["Divination", "Oracles", "Sooth Saying", "Prediction"]
			
			authorjob.extend(["Seer", "Oracle", "Shaman"])
			
			focus.extend(["Near Future", "Past", "Location", "Mind reading", "Far Future"])
			
			adjective.extend(["Accurate", "Real", "Veridict"])
			
		elif subselector < 3:
			output["branch"] = "protection"
			
			subjects = ["Protection", "Warding", "Hedging", "Shielding", "Abjuration"]
			
			authorjob.extend(["Warder", "Shaman"])
			
			focus.extend(["Personal", "Environmental", "Barriers", "Physical", "Duration"])
			
			adjective.extend(["Unbreakable"])
			
		elif subselector < 4:
			output["branch"] = "illusion"
			
			subjects = ["Illusion", "Ignis Fatuus", "Emulation", "Illusion", "Imitation"]
			
			authorjob.extend(["Illusionist", "Shaman", "Prestidigitator"])
			
			focus.extend(["Light", "Sound", "Sensation", "Detail", "Motion", "Duration"])
			
			adjective.extend(["Accurate", "Precise", "Perfect", "Meticulous"])
			
		elif subselector < 5:
			output["branch"] = "enchantment"
			
			subjects = ["Enchantment", "Manipulation", "Influence", "Control", "Hypnosis"]
			
			authorjob.extend(["Shaman"])
			
			focus.extend(["Mind Control", "Positive emotions", "Negative emotions", "Suggestions", "Duration", "Subtility"])
			
			adjective.extend(["Unbreakable", "Unshakable", "Perfect", "Meticulous"])
			
		elif subselector < 6:
			output["branch"] = "creation"
			
			subjects = ["Creation", "Apparition", "Creation"]
			
			authorjob.extend([])
			
			focus.extend(["Size", "Material", "Detail", "Complexity", "Duration"])
			
			adjective.extend(["Unbreakable", "Perfect", "Meticulous", "Precise"])
			
		elif subselector < 7:
			output["branch"] = "summoning"
			
			subjects = ["Summoning", "Invocation", "Awakening"]
			
			authorjob.extend(["Summoner", "Shaman"])
			
			focus.extend(["Demons", "Beasts", "Fay", "Elementals", "Necromancy", "Spirits"])
			
			adjective.extend(["Mighty", "Fierce", "Perfect", "Meticulous"])
			
		elif subselector < 8:
			output["branch"] = "movement"
			
			subjects = ["Movement", "Telekinesis"]
			
			authorjob.extend(["Shaman"])
			
			focus.extend(["Large items", "Several items", "Teleportation", "Flying", "Speed"])
			
			adjective.extend(["Precise", "Perfect", "Meticulous"])
			
		elif subselector < 9:
			output["branch"] = "channeling"
			
			subjects = ["Channeling", "Mana", "Energy","Thaumaturgy"]
			
			authorjob.extend(["Shaman", "Druid"])
			
			focus.extend(["Nodes", "Waylines", "Disenchantment", "Rate", "Duration"])
			
			adjective.extend(["Precise", "Perfect", "Meticulous"])
			
		elif subselector < 10:
			output["branch"] = "healing"
			
			subjects = ["Healing", "Biothaumaturgy", "Regeneration"]
			
			authorjob.extend(["Shaman", "Druid", "Doctor", "Priest"])
			
			focus.extend(["Wounds", "Deceases", "Resurrection", "Insanity", "Limb regrowth", "Several targets"])
			
			adjective.extend(["Precise", "Perfect", "Meticulous", "Wondrous", "Reliable"])
			
		elif subselector < 11:
			output["branch"] = "transformation"	
			
			subjects = ["Transformation", "Alteration", "Metamorphosis", "Transfiguration", "Transmutation"]
			
			authorjob.extend(["Shaman", "Druid", "Transmuter"])
			
			focus.extend(["Self transformation", "Animal transformation", "Material transformation"\
				, "Animating inanimate objects", "Several targets"])
			
			adjective.extend(["Precise", "Perfect", "Meticulous", "Wondrous", "Safe"])
			
		else:
			output["branch"] = "chronomancy"
			
			subjects = ["Chronomancy", "Time Manipulation", "Chronokinesis", "Time Bending"]
			
			authorjob.extend(["Chronomancer"])
			
			focus.extend(["Acceleration", "Slow down", "Leaps Forward"\
				, "Leaps Backwards", "Time Bubbles"])
			
			adjective.extend(["Precise", "Wondrous", "Safe"])
		
	elif selector < 10: #Humanities
		output["subject"] = "humanities"
		
		subselector = np.random.random()*7

		subjects = ["Humanities"]
			
		authorjob = ["Dilettante", "Scholar", "Noble"]
		
		focus = ["History", "Teaching", "Research", "Recent Development"]
		
		adjective.extend(["Advanced", "Modern", "Real", "Reliable", "Dynamic", "Effective", "Revolutionary", "Universal"])
		
		secret.extend(["The writer is a imposter with no knowledge of there subject"])
		
		if subselector < 1:
			output["branch"] = "sociology"
			
			subjects = ["Sociology", "Demography", "Structuralism"]
			
			authorjob.extend(["Sociologist"])
			
			focus.extend(["Culture", "Law and Punishment", "Communication", "Education", "Family", "Poverty and inequality"])
			
			adjective.extend(["Grounded"])
			
		elif subselector < 2:
			output["branch"] = "economics"
			
			subjects = ["Economics", "Finance", "Business", "Mercantilism"]
			
			authorjob.extend(["Economics", "Merchant"])
			
			focus.extend(["Markets", "Production", "Supply and demand", "Market failure", "Growth", "Inflation"])
			
			adjective.extend(["Grounded"])
			
		elif subselector < 3:
			output["branch"] = "psychology"
			
			subjects = ["Psychology", "Mind"]
			
			authorjob.extend(["Psychologist", "Mentalist"])
			
			focus.extend(["Biological", "Behavioral", "Cognitive", "Social", "Subconscious", "Motivation"])
			
			adjective.extend(["Human"])
			
		elif subselector < 4:
			output["branch"] = "political"
			
			subjects = ["Politics", "Political science", "Government", "Statecraft"]
			
			authorjob.extend(["Politician", "Statesman"])
			
			focus.extend(["Global", "Local", "Corruption", "Parties", "Policy", "Values", "Diplomacy"])
			
			adjective.extend(["Moral", "Popular"])
			
			
		elif subselector < 5:
			output["branch"] = "law"
			
			subjects = ["Law", "Legality", "Rules"]
			
			authorjob.extend(["Lawyer", "Judge"])
			
			focus.extend(["Philosophy", "Theory", "Military law", "Property law", "Criminal", "Bureaucracy", "Religious law"])
			
			adjective.extend(["Moral"])
			
			
		elif subselector < 6:
			output["branch"] = "ethics"
			
			subjects = ["Ethics", "Moral", "Morality", "Ethos"]
			
			authorjob.extend(["Philosopher"])
			
			focus.extend(["Businesses ethics", "Theory ethics", "Military ethics", "Political ethics", "Relationships", "Magic"])
			
			adjective.extend(["Proper"])
			
		else:
			output["branch"] = "philosophy"
			
			subjects = ["Philosophy", "Ideology", "Doctrine"]
			
			authorjob.extend(["Philosopher"])
			
			focus.extend(["Metaphysics", "Epistemology", "Value theory", "Logic", "	Philosophy of religion"])
			
			adjective.extend(["Proper", "Grounded"])
		
	else:
		output["subject"] = "language"
		
		subselector = np.random.random()*2

		subjects = ["Language"]
			
		authorjob = ["Linguist", "Scholar", "Noble"]
		
		focus = ["History", "Teaching", "Research", "Recent Development"]
		
		adjective.extend(["Advanced", "Modern", "Real", "Reliable", "Universal"])
		
		secret.extend(["The writer is a imposter with no knowledge of there subject"])
		
		if subselector < 1:
			output["branch"] = "dictionary"
			
			subjects = ["Dictionary", "Thesaurus", "Lexicon", "Glossary"]
			
			authorjob.extend(["Philosopher"])
			
			focus = ["Science", "Humanities", "Geography", "Religious", "Military", "Crafting"]
			
			adjective.extend(["Extensive", "Exhaustive", "Encyclopedic"])
		
			
		elif subselector < 2:
			output["branch"] = "translation"
			
			subjects = ["Translation", "Translation", "Lexicon", "Glossary", "Tongue"]
			
			authorjob.extend(["Explorer", "Translator"])
			
			focus = ["An arcane language", "A dead language", "A common language", "A rare language"]
			
			adjective.extend(["Extensive", "Exhaustive", "Encyclopedic"])
			
			
	aurthorfistname = np.random.choice(firstname)
	authorsurname = np.random.choice(surname)
	authorfullname = aurthorfistname + " " + authorsurname
	
	output["title"] = np.random.choice(namingscheme)
	
	output["title"] = output["title"].replace("@start@", str(np.random.choice(start)), 1)
	output["title"] = output["title"].replace("@adjective@", str(np.random.choice(adjective)), 1)
	output["title"] = output["title"].replace("@booktype@", str(np.random.choice(booktype)), 1)
	output["title"] = output["title"].replace("@random@", str(randomnamegenerator.main()), 1)
	output["title"] = output["title"].replace("@part1@", str(np.random.choice(part1)), 1)
	output["title"] = output["title"].replace("@part2@", str(np.random.choice(part2)), 1)
	output["title"] = output["title"].replace("@part1@", str(np.random.choice(part1)), 1)
	output["title"] = output["title"].replace("@part2@", str(np.random.choice(part2)), 1)
	output["title"] = output["title"].replace("@firstname@", str(np.random.choice(firstname)), 1)
	output["title"] = output["title"].replace("@surname@", str(np.random.choice(surname)), 1)
	output["title"] = output["title"].replace("@firstname@", str(np.random.choice(firstname)), 1)
	output["title"] = output["title"].replace("@surname@", str(np.random.choice(surname)), 1)
	output["title"] = output["title"].replace("@fullname@", str(np.random.choice(firstname)) + " " +\
		str(np.random.choice(surname)), 1)
	
	
	output["title"] = output["title"].replace("@authorsurname@", str(authorsurname), 1)
	output["title"] = output["title"].replace("@authorfullname@", str(authorfullname), 1)

	output["title"] = output["title"].replace("@subject@", str(np.random.choice(subjects)), 1)
	
	output["author"] = authorfullname
	output["authorjob"] = np.random.choice(authorjob)
	
	output["focus"] = np.random.choice(focus)
	if np.random.random() < 0.2:
		output["secret"] = np.random.choice(secret)
	else:
		output["secret"] = "no secret"
		
	output["state"] = np.random.choice(state)
	
	return(output)