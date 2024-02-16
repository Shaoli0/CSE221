f = open("input1.txt","r")
out=open("output1.txt", "w")
zone=int(f.readline())
match=f.readline()
match=match[0:len(match)-1]
prediction=f.readline()

def LCS(X,Y):
    m=len(X)+1
    p=len(Y)+1
    c=[[0 for i in range(m)] for j in range(p)]
    t=[[None for i in range(m)] for j in range(p)]
    for i in range(1,m):
        for j in range(1,p):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                t[i][j]="diagonal"
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                t[i][j]="up"
            else:
                c[i][j]=c[i][j-1]
                t[i][j]="left"
    
    string=""
    pointer1=pointer2=m-1
    while t[pointer1][pointer2]!=None:
        if t[pointer1][pointer2]=="diagonal":
            string+=X[pointer1-1]
            pointer1-=1
            pointer2-=1
        elif t[pointer1][pointer2]=="up":
            pointer1-=1
        else:
            pointer2-=1
    answer=[]
    for i in range(len(string)-1,-1,-1):
        if string[i]=="Y":
            answer.append("Yasnaya")
        elif string[i]=="R":
            answer.append("Rozhok")
        elif string[i]=="S":
            answer.append("School")
        elif string[i]=="P":
            answer.append("Pochinki")
        elif string[i]=="F":
            answer.append("Farm")
        elif string[i]=="M":
            answer.append("Mylta")
        elif string[i]=="H":
            answer.append("Shelter")
        else:
            answer.append("Prison")
    return answer
            
        
output=LCS(prediction,match)
print(output)
for i in range(len(output)):
    if i!=len(output)-1:
        out.write(output[i]+" ")
    else:
        out.write(output[i]+"\n")
    
correctness=(len(output)*100)//zone
out.write("Correctness of prediction:"+str(correctness)+"%")
out.close()