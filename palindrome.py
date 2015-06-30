#Checks if a string is Palindrome or not

import re
def pal(str1):
	if str1!=str1[::-1]:
		return -1
	else:
		return len(str1)
		
	