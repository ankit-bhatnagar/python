#Program to check if a string is a valid shuffle of 2 other strings using dynamic programming and caching results

def Shuffle(str1, str2, str3, cache=set()): 
	if (str1, str2) in cache: 
		return False   
	
	if len(str1)+len(str2)!=len(str3): 
		return False   
	
	if not str1 or not str2 or not str3: 
		if str1+str2==str3: 
			return True 
		else: 
			return False   
			
	if str1[0]!=str3[0] and str2[0]!=str3[0]: 
		return False  

	if str1[0]==str3[0] and Shuffle(str1[1:], str2, str3[1:], cache):
		return True 
	
	if str2[0]==str3[0] and Shuffle(str1, str2[1:], str3[1:], cache): 
		return True   
		
	cache.add( (str1, str2) )  

	return False