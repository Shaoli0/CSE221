f = open("input1.txt","r").read().split("\n")
out=open("output1.txt", "w")
n=int(f[0])
arr=f[1].split(" ")

def bubble_sort(A,n):
    for i in range(n-1):
        flag=False 
#For bubble sort,best case scenario is a sorted array.So,here we have assigned flag as false
#If flag stays false,then it means that no task is needed to be done and it will further not work on the array

        for j in range(n-i-1):
            a=int(A[j])
            b=int(A[j+1])
            if a>b:
                temp=a
                A[j]=b
                A[j+1]=temp
                flag=True
        if flag==False:
            break
bubble_sort(arr, n)

for i in arr:
    out.write(str(i)+" ")
     
out.close()           
    
            
        

