#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Copyright (c) 2010-2015 Russell Borogove. All rights reserved.

"""

import sys
import argparse
import os
import random
import numpy as np

from collections import defaultdict

HOME_FOLDER = os.path.dirname(sys.argv[0])
NAME_DATA_FOLDER = "namedata"

GREEK_ALPHABET = """Alpha
Beta
Gamma
Delta
Epsilon
Zeta
Eta
Theta
Iota
Kappa
Lambda
Mu
Nu
Xi
Omicron
Pi
Rho
Sigma
Tau
Upsilon
Phi
Chi
Psi
Omega""".split()

defaults = argparse.Namespace()
defaults.count = 1
defaults.min = 4
defaults.max = 13
defaults.new = False

# == MARKOV CHAIN BASED NAMER =========================================

class MarkovChainNamer( object ):
	def __init__(self):
		self.chains = defaultdict(list)
		self.splat = defaultdict(str)
		self.source = defaultdict(list)

	def next( self, setname, current ):
		if not current:
			return "^"
		k = current
		while True:
			if k:
				if (setname,k) in self.chains:
					return random.choice( self.chains[(setname,k)] )
				k = k[1:]
			else:
				return random.choice(self.splat[setname])

	def load_chains( self, setname, name ):
		if not name:
			return
		self.source[setname].append(name)
		name = "^" + name + "|"
		self.splat[setname] = self.splat[setname] + name
		# initials[setname] = initials[setname] + name[0]
		for count in range(2,4):
			for i in range(len(name)):
				seq = name[i:i+count]
				if len(seq) > 1:
					prefix = seq[:-1]
					self.chains[(setname,prefix)].append( seq[-1] )


	def load_dataset_file( self, setname, filepath ):

		with open(filepath, encoding='utf-8') as f:
			names = f.read().splitlines() 

		for name in names:
			if name.startswith('#'):
				continue
			# Keep everything as unicode internally
			self.load_chains( setname, name )
			self.load_chains( "all", name )

	
	def load_dataset( self, setname ):
		if setname == "all":
			self.load_all_name_data()
		else:			 
			path = os.path.join( HOME_FOLDER, NAME_DATA_FOLDER, setname+".txt" )
			if os.path.exists(path):
				self.load_dataset_file( setname, path )
			else:
				print ("Error: name data file '%s' not found."%path)
				sys.exit(-1)
			
	def load_all_name_data(self):
		for fn in os.listdir( os.path.join( HOME_FOLDER, NAME_DATA_FOLDER ) ):
			if fn.endswith(".txt"):
				setname, ext = os.path.splitext(fn)
				path = os.path.join( HOME_FOLDER, NAME_DATA_FOLDER, setname+".txt" )
				self.load_dataset_file( setname, path )

	def _gen_name( self, setname, options ):
		ok = False
		
		if setname not in self.splat:
			self.load_dataset(setname)

		while not ok:
			name = "^"
			
			while len(name) < options.max:
				next = self.next( setname, name )
				if next != "|":
					name += next
				else:
					if len(name) > options.min:
						ok=True
					break

		return name.replace("^","")

	def gen_name( self, setname, options ):
		acceptable = False
		while not acceptable:
			name = self._gen_name( setname, options )
			if not options.new:
				acceptable = True
			else:
				# compare the generated name against existing names for the set
				if name not in self.source[setname]:
					acceptable = True
		return name	   

# == SELECTOR =========================================================

markov = MarkovChainNamer()

# A function to name a star using Bayer-style names in made-up
# constellations with pseudo-latin names.
def gen_star_name( options = defaults ):
	# Generate a pseudo-latin constellation name.
	if random.randrange(2):
		constellation = markov.gen_name( "latinm", options )
	else:													  
		constellation = markov.gen_name( "latinf", options )

	# Choose a rank for the star within the constellation;
	# making the brighter ranks (Alpha, Beta...) more likely
	# because we're magnitude elitists.
	rank = random.randrange(5)
	while random.randrange(2):
		rank += 1
	# Take that ranked Greek letter; if we rolled an
	# extraordinarily high rank, just wrap around the list.
	rankname = GREEK_ALPHABET[ rank % 24 ]

	# for example, "Epsilon Athanatille"
	return "%s %s"%(rankname,constellation)


# Generate a "full name" given a sequence
def names(gen, sourceSequence, minlen = 4, maxlen = 10, new = False) : 
	generated = []
	
	options = argparse.Namespace()
	options.count = 1
	options.min = minlen
	options.max = maxlen
	options.new = new

	if gen:
		for source in sourceSequence:
			generated.append( markov.gen_name( source, options ) )
	else: 
		for source in sourceSequence:
			if source not in markov.splat:
				markov.load_dataset(source)
			generated.append(np.random.choice(markov.source[source]))
	return " ".join(generated)

def gen_names( sourceSequence, options = defaults ):
	generated = []
	for source in sourceSequence:
		generated.append( markov.gen_name( source, options ) )

	return " ".join(generated)
	
def name(gen, setname, lenght = [4,10], new = False): 


	if gen:
		options = argparse.Namespace()
		options.count = 1
		options.min = lenght[0]
		options.max = lenght[1]
		options.new = new
		return markov.gen_name( setname, options )
	else:
		if setname not in markov.splat:
			markov.load_dataset(setname)
		namelist = []
		for i in range(9):
			namelist.append(np.random.choice((markov.source[setname]))) 
			if len(namelist[i]) >= lenght[0] and len(namelist[i]) <= lenght[1]:
					return namelist[i]
					break
		else:
			if(len(max(namelist, key=len)) < lenght[0]):
				return max(namelist, key=len)
			if(len(min(namelist, key=len)) > lenght[1]):
				return min(namelist, key=len)

def gen_name( setname, options = defaults ):
	return markov.gen_name( setname, options )
	

def randname(lenght):

	consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z", "w"]
	vowels = ["a", "e", "i", "o", "u", "y"]
	mean = int((lenght[0]+lenght[1])/2) 
	
	letternum = random.triangular(lenght[0],mean,lenght[1])
	name = ""
	
	if random.random() > 0.5:
		name = name + random.choice(consonants)
		c = 1
	else:
		name = name + random.choice(vowels)
		c = 0
		
	while len(name) < letternum:
	
		if c == 1: 
			if random.random() > 0.98:
				name = name + random.choice(consonants)
				c = 1
			else:
				name = name + random.choice(vowels)
				c = 0
				
		if c == 0: 
			if random.random() < 0.98:
				name = name + random.choice(consonants)
				c = 1
			else:
				name = name + random.choice(vowels)
				c = 0
	
	return(name.capitalize())

# =====================================================================

def tests():
	# Generate a star name.
	print (gen_star_name())

	# Generate an individual person's full name - in this case, a pseudo-French woman
	# with a quasi-Japanese father, whose mother read a lot of fantasy novels.
	# example result: Jestée Lyona Harasahiro
	print (gen_names( ["frenchf","arthurianf","japansur"] ))

	# Produce several pages of names for your RPG setting - print 'em out, and
	# when you introduce an NPC, pick a name off an appropriate list and cross it off.
	groups = [	("Island Provinces", ["arthurianm", "arthurianf", "normanm", "normanf", "normansur", "saxonm", "saxonf"] ),
				("Western Lands", ["albanianm", "albanianf" ] ),
				("Old Lands", ["provinces","engbynames","englocalities","engtradenames"] ),
				("Desert Nomads", ["arabicm","arabicf"] ),
				("Other", ["all"] ) ]

	for group,setnames in groups:
		print ("%s Names"%group)
		for name in range(3):
			col1 = gen_name( random.choice(setnames) )
			col2 = gen_name( random.choice(setnames) )
			col3 = gen_name( random.choice(setnames) )
			print ("  %15s %15s %15s\n"%(col1,col2,col3))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument( '--count', help="number of names to generate", type=int, default=1 )
	parser.add_argument( '--sequence', help="use name sets in order instead of randomly", action='store_true', default=False )
	parser.add_argument( '--star', help="generate a star name in a fictional constellation", action='store_true',default=False )
	parser.add_argument( '--min', help="minimum name length", type=int, default=4 )
	parser.add_argument( '--max', help="maximum name length", type=int, default=13 )
	parser.add_argument( '--new', help="reject names appearing in source data", action='store_true', default=False )

	options,sets = parser.parse_known_args( sys.argv[1:] )

	if not sets:
		sets = ["all"]
	results = []
	if options.star:
		results = [ gen_star_name( options ) for _ in range( options.count ) ]
	elif options.sequence:
		results = [ gen_names( sets, options ) for _ in range( options.count ) ]
	else:
		results = [ gen_name( random.choice( sets ), options ) for _ in range( options.count ) ]

	for result in results:
		print (result)
