#Hacker Rank
# Performing various functions on a List
L=[]
def match(c):
	if c[0]=='insert':
		L.insert(int(c[1]),int(c[2]))
	elif c[0]=='print':
		print L
	elif c[0]=='remove':
		L.remove(int(c[1]))
	elif c[0]=='append':
		L.append(int(c[1]))
	elif c[0]=='sort':
		L.sort()
	elif c[0]=='reverse':
		L.reverse()
	elif c[0]=='pop':
		L.pop()
	else:
		return
	
N=int(raw_input())
for i in range(N):
    command=raw_input()
    c=command.split()
    match(c)
