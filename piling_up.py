#Piling up challenge
def result(nums,n):
	numbers=[]
	for i in nums:
		numbers.append(int(nums[i]))
	j=n-1
	for i in range(n):
		if numbers[i]>=numbers[j]:
			pass


T=int(raw_input())
for t in range(T):
	#test cases
	n=int(raw_input())
	text=raw_input()
	text2=text.split()
	result(text2,n)

