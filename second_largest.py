# Program to print the 2nd largest number
def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

num=int(raw_input())
text=raw_input()
text2=text.split()
numbers=[]
for i in range(num):
	numbers.append(int(text2[i]))
value=second_largest(numbers)
print value