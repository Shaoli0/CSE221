adj_list={}
f = open("input.txt","r")
out=open("output3.txt", "w")
endPoint=f.readline()#stored endPoint in string
for i in f:
    splitted=i.split()
    adj_list[splitted[0]]=[]
    for j in range(1,len(splitted)):
        adj_list[splitted[0]].append(splitted[j])
        
visited=[0]*int(endPoint)
printed=[]
def dfs_visit(graph,node):
    visited[int(node)-1]=1
    printed.append(node)
    for i in graph[node]:
        if visited[int(i)-1]==0:
            dfs_visit(graph,i)
            
def dfs(graph,end):
    for i in graph:
        if visited[int(i)-1]==0:
            dfs_visit(graph,i)
        
    for i in printed:
        out.write(i +" ")
        if i==end:
            break

dfs(adj_list,"12")


out.close()