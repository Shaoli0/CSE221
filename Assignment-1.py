def binary_search(a,b,A,B):
    for i in range(0,b):
        left=0
        right=a-1
        count=0
        while left<=right:
            M=(left+right)//2
            if B[i]<A[M]:
                count=M
                right=M-1
            elif B[i]==A[M]:
                count=M+1
                left=M+1
            else:
                left=M+1
        print(count,end=" ")
binary_search(8,3,[1,1,2,5,5,5,5,6],[5,3,2])               
                

