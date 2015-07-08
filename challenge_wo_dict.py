#Container challenge without dictionary

def comparison(words1,words2):

    for b in range(len(words2)):
        #resetting value for checking next
        location=[]
        found=0
        for a in range(len(words1)):
            if words2[b]==words1[a]:
                found=1
                location.append(a+1)
            else:
                pass
            
        if found==1:
            #output the locations
            for l in range(len(location)):
                print location[l],
            print "\n",
        else:
            print "-1"


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

comparison(A,B)
    