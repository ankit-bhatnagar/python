#Piling up challenge
def result(nums,n):
	numbers=[]
	for i in range(len(nums)):
		numbers.append(int(nums[i]))
	looping(numbers)

def check_desc(final):
	for i in range(len(final)):
		if i==len(final)-1:
			continue
		elif final[i]>=final[i+1]:
			continue
		else:
			return "No"
	return "Yes"		

def looping(numbers):
	#compare repeatedly the 1st n last elements
	final=[]
	for i in range(len(numbers)):
		if numbers[0]>=numbers[len(numbers)-1]:
			final.append(numbers.pop(0))
		else:
			final.append(numbers.pop())
	ans=check_desc(final)
	print ans
	#store the popped elements and later check if in descending order

T=int(raw_input())
for t in range(T):
	#test cases
	n=int(raw_input())
	text=raw_input()
	text2=text.split()
	result(text2,n)
