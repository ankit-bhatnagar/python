#lexicon file

#scan function

def check_number(text):
	try:
		return int(text)
	except ValueError:
		return None

 
def scan(text):
	#make tuples for each text possible
	directions=('north','south','east','west')
	verbs=('go','kill','eat')
	stops=('the','in','of')
	nouns=('bear','princess')
	#check if a digit is a number
	#if anything else then pair it with error!!

	#use split and put that into a list
	values=text.split()
	final=[]

	for v in values:
		if v in directions:
			final.append(('direction',v))
		elif v in verbs:
			final.append(('verb',v))
		elif v in stops:
			final.append(('stop',v))
		elif v in nouns:
			final.append(('noun',v))
		elif check_number(v):
			final.append(('number',check_number(v)))	
		else:
			final.append(('error',v))
	return final