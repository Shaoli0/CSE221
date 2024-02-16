f = open("task3_input.txt","r")
out=open("output3.txt", "w")
tasks=int(f.readline())
S=f.readline().split()
string=f.readline()
S.sort()

stack=[]
index=0
Jack=0
sequence=""
Jill=0

for i in string:
    if i=="J":
        stack.append(S[index])
        sequence+=(S[index])
        Jack+=int(S[index])
        index+=1
    elif i=="j":
        u=stack.pop()
        sequence+=u
        Jill+=int(u)      
print(sequence)
for i in sequence:
    out.write(i)
    
out.write("\n")

out.write("Jack will work for"+" "+str(Jack)+" "+"hours"+"\n")
out.write("Jill will work for"+" "+str(Jill)+" "+"hours")
out.close()