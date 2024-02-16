from heapq import heappush,heappop

f = open("input4.txt","r")
out=open("output4.txt", "w")
testCase=int(f.readline())

        
def Network(graph,s):
    n=int(v_And_e[0])
    dist=[-100]*n
    dist[s-1]=100
    Q=[]
    prev=[0]*n
    for i in graph:
        heappush(Q, (-1*dist[int(i)-1], i))
                 
    while len(Q)!=0:
        
        u=heappop(Q)[1]
        if u in graph:
            
            for v in graph[u]:
                alt=min(dist[int(u)-1],int(v[1]))
                if alt>dist[int(v[0])-1]:
                    dist[int(v[0])-1]=alt
                    prev[int(v[0])-1]=u

                    heappush(Q,(-1*alt,v[0]))
    
                    
    for i in dist:
        if i == 100:
            out.write("0"+" ")
        elif i==-100:
            out.write("-1"+" ")
        else:
            out.write(str(i)+" ")
    out.write("\n")


for i in range(testCase):
    v_And_e=f.readline().split()
    if int(v_And_e[1])==0:
        out.write(str(0)+"\n")
        f.readline()
    else:
        adj_list={}
        for i in range(int(v_And_e[1])):
            splitted=f.readline().split()
            if splitted[0] not in adj_list:
                adj_list[splitted[0]]=[]
            adj_list[splitted[0]].append(splitted[1:])
        source=int(f.readline())

        Network(adj_list,source)
        
out.close()