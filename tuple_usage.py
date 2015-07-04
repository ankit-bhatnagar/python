# Working on a tuple

a=int(raw_input())
b=raw_input()
list_b=b.split()
list2=[]
for i in range(a):
    list2.append(int(list_b[i]))
t=tuple(list2)
print hash(t)
