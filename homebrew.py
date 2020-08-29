import math

def arrayreader(filename):

	list_of_lists = []

	with open(filename, encoding='UTF-8') as f:
		for line in f:
			inner_list = [elt.strip() for elt in line.split(';')]
			# in alternative, if you need to use the file content as numbers
			# inner_list = [int(elt.strip()) for elt in line.split(',')]
			list_of_lists.append(inner_list)
			
	return(list_of_lists)
	
def arraycleaner(listoflist, index):
	i = 0
	for i in listoflist:
		del i[index]
		
	return(listoflist)
			
	
	
def rotate(array):

	rotated = list(map(list, zip(*array)))
	
	return(rotated)
	
	
def sigfig(x, digit):
	try:
		return round(x, digit -1 -int(math.floor(math.log10(abs(x)))))
	except ValueError:
		return round(x, digit -1)
def normalise(list):
	return([float(i)/sum(list) for i in list])