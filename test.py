
num=[1,8,3,5,9,4]
for i in range(len(num)):
	if num[0]<num[len(num)-1]:
		print "deleting"
		num.pop()
	
print num	