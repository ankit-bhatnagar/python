#Program to find if a pattern exists in a text

import re

def find_pattern(pattern,text):
	for match in re.findall(pattern, text):
	    print 'Found "%s"' % match