#Container challenge with dictionary
from collections import defaultdict

def comparison(words1,words2):
    answer=defaultdict(list)
    for b in range(len(words2)):
        #resetting value for checking next
        found=0
        for a in range(len(words1)):
            if words2[b]==words1[a]:
                found=1
                answer[words2[b]].append(a+1)
            else:
                pass
        if found==0:
            answer[words2[b]].append(-1)        
    return answer

text=raw_input()
text_2=text.split()
n=int(text_2[0])
m=int(text_2[1])
A=[]
B=[]
for i in range(n):
    word=raw_input()
    A.append(word) 

for j in range(m):
    word2=raw_input()
    B.append(word2)

ans=comparison(A,B)
for b in B:
    for i in range(len(ans[b])):
        print ans[b][i],
    print "\n",    