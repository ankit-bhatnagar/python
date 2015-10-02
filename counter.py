# Counter collections program
from collections import Counter

x=int(raw_input())
all_sizes=raw_input()
size_list=all_sizes.split()
size_numbers=[]
for i in range(x):
    size_numbers.append(int(size_list[i]))
money=0
n=int(raw_input()) #customers
for j in range(n):
    cust_input=raw_input()
    cust_parts=cust_input.split()
    if int(cust_parts[0]) in size_numbers:
        money=money+int(cust_parts[1])
        size_numbers.remove(int(cust_parts[0]))
    
#print Counter(size_numbers)
print money
