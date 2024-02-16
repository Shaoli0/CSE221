from heapq import heappush,heappop

f = open("input1.txt","r")
out=open("output1.txt", "w")
testCase=int(f.readline())
def dijkstra(graph,source):
    n=int(v_And_e[0])
    
    dist=[100]*n
    dist[source-1]=0
    prev=[0]*n
    visited=[False]*n
    Q=[]
    for i in graph:
        heappush(Q,(i,dist[int(i)-1]))
        
    while len(Q)!=0:
        u=heappop(Q)
        if visited[int(u[0])-1]==True:
            continue
        
        visited[int(u[0])-1]=True
        for v in graph:
            for neighbours in graph[v]:
                alt=dist[int(v)-1]+int(neighbours[1])
                if alt<dist[int(neighbours[0])-1]:
                    dist[int(neighbours[0])-1]=alt
                    prev[int(neighbours[0])-1]=v
                    heappush(Q,(neighbours[0],dist[int(neighbours[0])-1]))
    output=max(dist)
    out.write(str(output)+"\n")
    
    
        
                    
     
for i in range(testCase):
    v_And_e=f.readline().split()
    if int(v_And_e[1])==0:
        out.write(v_And_e[1]+"\n")
        
        
    else:
        adj_list={}
        for i in range(int(v_And_e[1])):
            splitted=f.readline().split()
            if splitted[0] not in adj_list:
                adj_list[splitted[0]]=[]
            adj_list[splitted[0]].append(splitted[1:])
            #print(adj_list)
        dijkstra(adj_list,1)
           
out.close()        
    

    