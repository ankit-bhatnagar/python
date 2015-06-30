#Program to check if the 2 words are anagrams of each other or not

import collections

def isAnagram2(str1, str2): 
   if len(str1)!=len(str2): 
	return False 
	
   string1=str1.lower()
   string2=str2.lower()
   counts=collections.defaultdict(int)
   for letter in string1: 
	counts[letter]+=1 
   for letter in string2: 
	counts[letter]-=1 
	if counts[letter]<0: 
		return False 
   return True