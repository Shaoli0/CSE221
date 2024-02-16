f = open("input2.txt","r")
out=open("output2.txt", "w")
string1=f.readline()
string1=string1[0:len(string1)-1]
string2=f.readline()
string2=string2[0:len(string2)-1]
string3=f.readline()

def LCS(X,Y,Z):
    str1=len(X)+1
    str2=len(Y)+1
    str3=len(Z)+1            
    c=[[[0 for i in range(str3)] for j in range(str2)] for k in range(str1)]
    t=[[[None for a in range(str3)] for b in range(str2)] for d in range(str1)]
    for i in range(1,str1):
        for j in range(1,str2):
            for k in range(1,str3):
                if X[i-1]==Y[j-1] and X[i-1]==Z[k-1]:
                    c[i][j][k]=c[i-1][j-1][k-1]+1
                    t[i][j][k]="diagonal"
                else:
                    if c[i-1][j][k]>=c[i][j-1][k]:
                        maximum=c[i-1][j][k]
                        if maximum>=c[i][j][k-1]:
                            c[i][j][k]=maximum
                            t[i][j][k]="up-up-left"
                        else:
                            maximum=c[i][j][k-1]
                            c[i][j][k]=maximum
                            t[i][j][k]="left-up-up"
                    else:
                        maximum=c[i][j-1][k]
                        if maximum>=c[i][j][k-1]:
                            c[i][j][k]=maximum
                            t[i][j][k]="up-left-up"
                        else:
                            maximum=c[i][j][k-1]
                            c[i][j][k]=maximum
                            t[i][j][k]="left-up-up"
    out.write(str(c[str1-1][str2-1][str3-1]))
LCS(string1,string2,string3)
out.close()                        