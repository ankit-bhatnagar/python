#Program to sort words in a string according to their length

import re
import collections
def sort(str1):
	str2=str1.split()
	values=collections.defaultdict(int)
	min=0
	for i in str2:
		values[i]=(len(i))
	
	print sorted(values,key=values.get)