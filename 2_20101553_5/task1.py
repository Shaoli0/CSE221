f = open("task1_input.txt","r")
out=open("output1.txt", "w")
row=int(f.readline())
arr=[]
for i in range(row):
    col=f.readline().split()
    arr.append(col)

def Assignment_selection(array,n):
    array.sort(key = lambda x: int(x[1]))
    selected=[]
    selected.append(array[0])
    f=int(array[0][1])
    
    
    for i in range(1,len(array)):
        if int(array[i][0])>=int(f):
            f=array[i][1]
            selected.append(array[i])
    return selected

output=(Assignment_selection(arr,row))


out.write(str(len(output))+"\n")
for i in range(len(output)):
    for j in range(len(output[0])):
        out.write(output[i][j]+" ")
    if i==len(output)-1:
        break
    else:
        out.write("\n")
out.close()