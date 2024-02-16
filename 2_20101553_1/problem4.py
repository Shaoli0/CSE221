f = open("input4.txt", "r").read().split("\n")
out=open("output4.txt", "w")
n=int(f[0])
A=[]
B=[]

count=1

for i in range(1,len(f)):
    if count<=n:
        count+=1
        A.append(f[i].split())
    elif i==n+1:
        pass
    else:
        B.append(f[i].split())

C = [[0]*(len(A)) for k in range(len(B))]
for i in range(n):
    for j in range(n):
        for k in range(n):           
            C[i][j] +=int(A[i][k]) * int(B[k][j])
            
for i in range(n):
    for j in C[i]:
        out.write(str(j)+" ")
    out.write("\n")

out.close()