adj_list={}
f = open("input.txt","r")
out=open("output2.txt", "w")
endPoint=f.readline()#stored endPoint as string
for i in f:
    splitted=i.split()
    adj_list[splitted[0]]=[]
    for j in range(1,len(splitted)):
        adj_list[splitted[0]].append(splitted[j])


visited=[0]*int(endPoint)#Used the endPoint to create the list of visited
queue=[]
def bfs(v,graph,node,lastNode):
    v[int(node)-1]=1
    queue.append(node)
    while(len(queue)!=0):
        m=queue.pop(0)
        out.write(m +" ")
        
        if m==lastNode:
            break
        for i in graph[m]:
            if v[int(i)-1]==0:
                v[int(i)-1]=1
                queue.append(i)
bfs(visited,adj_list,"1","12")
out.close()