#Piling up challenge
def result(nums,n):
	numbers=[]
	for i in range(len(nums)):
		numbers.append(int(nums[i]))
	print numbers
	looping(numbers)

def looping(numbers):
	#compare repeatedly the 1st n last elements
	for i in range(len(numbers)):
		if numbers[0]>=numbers[len(numbers)-1]:
			pass
		else:
			numbers.pop()	
	print numbers
	#store the popped elements and later check if in descending order

T=int(raw_input())
for t in range(T):
	#test cases
	n=int(raw_input())
	text=raw_input()
	text2=text.split()
	result(text2,n)
