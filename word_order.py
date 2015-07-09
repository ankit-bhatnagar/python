#Word order challenge
from collections import OrderedDict

groups=OrderedDict()
n=int(raw_input())
for i in range(n):
	text=raw_input()
	if text not in groups:
		groups[text]=1
	else:
		groups[text]+=1

print len(groups)
for g in groups:
    print groups[g],