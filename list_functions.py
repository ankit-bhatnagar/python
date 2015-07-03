# Enter your code here. Read input from STDIN. Print output to STDOUT
L=[]
def match(c):
    if c[0]=='insert':
        L.append(c[1])
        L.append(c[2])
    elif c[0]=='print'    
    
N=int(raw_input())
for i in range(N):
    command=raw_input()
    c=command.split()
    match(c)