#Program to find the location of a word in the given text and return all positions

import collections
import re
def location(word,text): 
	index=collections.defaultdict(list) 
	words=(text.lower()).split() 
	for pos, word2 in enumerate(words): 
		index[word2].append(pos) 
		print type(pos), " ", word2
	if word in index:
		return index[word]
	else:
		return False