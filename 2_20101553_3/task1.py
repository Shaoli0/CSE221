adj_list={}#Used dictionary to take the adjacency list as input
f = open("input.txt","r")
endPoint=f.readline()#stored endPoint in string
for i in f:
    splitted=i.split()
    
    adj_list[splitted[0]]=[]
    for j in range(1,len(splitted)):
        adj_list[splitted[0]].append(splitted[j])

print(adj_list)#Created graph