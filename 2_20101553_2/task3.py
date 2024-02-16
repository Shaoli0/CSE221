f = open("input3.txt","r").read().split("\n")
out=open("output3.txt", "w")

n=int(f[0])

ID=f[1].split(" ")
number=f[2].split(" ")



def insertion_sort(A,B,n):#A=number,B=ID
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if(int(A[j])<int(A[j+1])):
                temp=B[j]
                temp1=A[j]
                B[j]=B[j+1]
                A[j]=A[j+1]
                B[j+1]=temp
                A[j+1]=temp1
            else:
                break
insertion_sort(number,ID,n)

for i in ID:
    out.write(i+" ")
 
    
out.close()
        


