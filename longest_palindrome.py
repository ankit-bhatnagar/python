#Program prints the longest palindrome present in the text 

import palindrome
import collections
def long(str1):
	str2=str1.split()
	values=collections.defaultdict(int)
	max=0
	seen=0
	for i in str2:
		values[i]=(palindrome.pal(i))
	
	for v in values:
		if values[v]>max:
			max=values[v]
		
	for v in values:
		if values[v]==max:
			print v
			seen=1
	if seen==0:
		print "No palindrome present in the text"