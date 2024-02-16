f = open("input2.txt","r").read().split("\n")
out=open("output2.txt", "w")

num=f[0].split(" ")
N=int(num[0])
M=int(num[1])
arr=f[1].split(" ")
stop=0
import numpy as np
for i in range(len(arr)):
    a=int(arr[i])
    
    arr[i]=a
    
lst=np.array(arr)
 
for i in range(N):
    if stop==M:
        break
    else:
        stop+=1
        m=lst.argmin()
        temp=lst[m]
        lst[m]=arr[i]
        arr[m]=lst[m]
        arr[i]=temp
        
        
for i in range(M):
    out.write(str(arr[i])+" ")
        


out.close()