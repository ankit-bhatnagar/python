# A happiness challenge

text=raw_input()
text2=text.split()

array_input=raw_input()
check_array=[]
values=array_input.split()
for i in range(len(values)):
	check_array.append(int(values[i]))
answer=0
set_n=set()
set_m=set()
input_n=raw_input()
input_m=raw_input()
values_n=input_n.split()
values_m=input_m.split()

for i in range(len(values_n)):
	set_n.add(int(values_n[i]))
for i in range(len(values_m)):
	set_m.add(int(values_m[i]))

for a in check_array:
	if a in set_n:
		answer=answer+1
	else:
		continue

for a in check_array:
	if a in set_m:
		answer=answer-1
	else:
		continue

print answer
