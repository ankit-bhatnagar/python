#Program displays the count of each character in a text

import re
import collections
def count(str):
	
	values=collections.OrderedDict()
	#for arbitrary order can use defaultdict
	#values=collections.defaultdict(int)
	
	for i in str:
		values[i]=0
	
	for i in str:
		values[i]+=1
	
	for j in values:
		print "'%s' : %d" %(j,values[j])
		
			
	