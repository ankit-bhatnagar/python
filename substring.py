# Program to output the no. of occurrances of a substring
import collections
import re
def exists(word,text):
	global count
	match=re.search(word,text)
	if match:
		i=match.start()
		count+=1
		if count<len(text):
			exists(word,text[i+1:])
count=0	
text=raw_input()
word=raw_input()
exists(word,text)
print count