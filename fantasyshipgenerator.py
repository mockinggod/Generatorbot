# Port and at sea

# Explorers / Fishing / Flotilla Town / Mercenary / Merchant / Messenger / Missionary / Monster Hunters / Navy / Pirate / Pleasure / Prison / Private / Privateers / Raider / Slaver / Smuggler

# Small / Medium / Large / Huge / Gargantuan

# Cargo Capacity / Combat (boarding) / Combat (ranged) / Long Voyage / Luxury / Smuggling / Speed / Troop Capacity

# Raft / Barge / Escort / Scout / War ship / Dreadnaught / Transport (Supply, Troop) / Cargo ship

# good / worn but sea worthy / damaged /  falling apart

# Crew Type (people) - human / non-human / mixed / all women / no crew

# Crew Type (monster) - automatons / demons / monsters / ghosts / golems / undead / zombies

# At sea

# Sinking cause - enemy ship / iceberg / monster / reef / sabotage / storm / tidal wave / whirl pool / unknown

# Cursed - frozen in ice / frozen in time / turned to stone / transformed into animals

# Dead - signs of a fight / signs of monsters / no signs of a struggle / diseased / poisoned / starvation

# Plagued - contagious disease / faking it

# Lone Survivor - holding bloody saver, knife, or table leg / chained to mast / in metal cage / in magic circle drawn on floor / eating someone s arm

# Lone Survivor(2) - attacks / ask to be taken to x location / speaks gibberish / too terrified to speak / motions you to be silent & points at the cargo hold / begs you to kill him / transforms into a monster / monster eats its way out of survivor

# Fighting (crew vs) - 1 man / boarding crew / 1 monster / many monsters / horde of tiny monsters

# Massacred - killed by weapons / killed by monsters (still onboard?) / killed each other / calling card of x / half eaten

# Missing - signs of a fight / signs of monsters / calling card of x / no signs (mystery)

# Format

# Main descriptor state + job + bonus + action
# secret
# Cargo

# captain
# crew descriptor 

import numpy as np
import homebrew as hb

def main(situation = None):

	output = {}

	port = False
	sail = False
	drift = False
	reck = False
		
	if (situation == "port" or situation == "p"):
		port = True
		
	if (situation == "sailing" or situation == "sail"):
		sail = True	
		
	if (situation == "drifting" or situation == "drift" or situation == "d"):
		drift = True	
		
	if (situation == "recked" or situation == "reck" or situation == "r"):
		reck = True	
		
	if (situation == "sea" or situation == "s" ):
		if np.random.random() < 0.8:
			sail = True
		else:
			drift = True
			
	bonus = (hb.arrayreader("medievalshipbonus.txt"))
	bonus+= (hb.arrayreader("fantasyshipbonus.txt"))


	# with open("medievalshipsecret.txt", encoding='latin-1') as f:
		# secret = f.read().splitlines() 
		
	# with open("fantasyshipsecret.txt", encoding='latin-1') as f:
		# secret += f.read().splitlines() 
		
	# with open("medievalcargo.txt", encoding='latin-1') as f:
		# cargo = f.read().splitlines() 
		
	# with open("fantasycargo.txt", encoding='latin-1') as f:
		# cargo += f.read().splitlines() 
	
		
	states = ["A brand new",\
		"A like-new",\
		"A small",\
		"A large",\
		"A huge",\
		"A worn",\
		"A worn, but sea worthy",\
		"An old",\
		"An old, but very well maintained",\
		"An ancient"\
		]
		
	jobs = ["exploration",\
		"fishing",\
		"diplomatic",\
		"mercenary",\
		"merchant",\
		"missionary",\
		"monster hunting",\
		"naval",\
		"pleasure",\
		"privateer",\
		"slaver"\
		]
	

	
	actions = []

	if port:
		states.extend(["A still unvarnished"])
		bonus.extend([\
			["with [[a party/a brawl/a wedding/an unknown contest]] ongoing on deck",4]])
		actions.extend(["is docked", "is being unloaded", "is being loaded", "is having its hull inspected", "is undergoing simple maintenance", "is getting ready to set sail"])
	else:
		jobs.extend(["pirate", "raider"])
	
	if sail:
		bonus.extend([\
			["followed [[dolphins/sharks/seagulls/an albatross]]",4]\
			["with a [[party/brawl/wedding/unknown contest]] ongoing on deck", 4]])
			
		actions.extend(["is sailing ahead and you are catching up", "is sailing behind you and catching up", "is sailing towards you"])
	
	if drift:
		bonus.extend([\
			["with a [[broken/shattered/missing mast]]",4]])
		actions.extend(["is [[slowly//rapidly]] drifting northwards","is [[slowly//rapidly]] drifting eastwards","is [[slowly//rapidly]] drifting southwards","is [[slowly//rapidly]] drifting westwards", "is floating [[very/]] low in the water", "is drifting in a circle around its lowered anchor"])
	
	if reck:
		states.extend(["A rotting", "A broken"])
		actions.extend(["is grounded on the shore","is laying on its side","is grounded on a reef"])
	else:
		bonus.extend([\
			["with ripples around the hull forming complex patterns that convey [[calm/anger/joy/excitement/impatience]]",0.3]])
	
	if situation == None:
		actions.extend([""])
		
	bonus = (hb.rotate(bonus))
	bonus[1][:] = [float(p) for p in bonus[1]]
	s = sum(bonus[1])
	bonus[1][:] = [p/s for p in bonus[1]]
		
		
	output["descriptor"] = np.random.choice(states) + " " + np.random.choice(jobs) + " [[vessel/ship]] " + np.random.choice(bonus[0], p=bonus[1]) + " " + np.random.choice(actions)
	# output["secret"] = np.random.choice(secret)
	# output["cargo"] = np.random.choice(cargo)
	
	return(output)