f = open("task2_input.txt","r")
out=open("output2.txt", "w")
row_people=f.readline().split()
row=int(row_people[0])
pep=int(row_people[1])

arr=[]
for i in range(row):
    col=f.readline().split()
    arr.append(col)

people=[[0 for i in range(2)] for j in range(pep)]

def activities_completed(array,n):
    array.sort(key = lambda x: int(x[1]))
    
    selected=[]
    for i in range(n):
        selected.append(array[i])
        people[i]=array[i]
    i=len(people)
    while i<len(array):
        for j in range(len(people)):
            if int(array[i][0])>=int(people[j][1]):
                people[j]=array[i]
                selected.append(array[i])
                break
        i+=1
    return selected
    
output=activities_completed(arr,pep)
out.write(str(len(output)))
out.close()