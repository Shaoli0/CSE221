def merge(array1,array2):#array1=left array,array2=right
    length=len(array1)+len(array2)
    C=[0]*length
    i=0 #Left array index
    j=0 #Right array index
    index=0 #merge and sorted array index
    while i<len(array1) and j<len(array2):
        if int(array1[i])<int(array2[j]):
            C[index]=array1[i]
            i+=1
        else:
            C[index]=array2[j]
            j+=1
        index+=1
    while i<len(array1):
        C[index]=array1[i]
        i+=1
        index+=1
    while j<len(array2):
        C[index]=array2[j]
        j+=1
        index+=1
    return C
        
            
def merge_sort(array):
    if len(array)>1:
        m=len(array)//2
        left=merge_sort(array[:m])
        right=merge_sort(array[m:])
        return merge(left,right)
    else:
        return array



f = open("input4.txt","r").read().split("\n")
out=open("output4.txt", "w")
n=int(f[0])
array=f[1].split(" ")
answer=merge_sort(array)
for i in answer:
    out.write(i+" ")
out.close()

