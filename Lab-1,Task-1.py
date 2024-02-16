class percentage: 
    def __init__(self):
        f = open("input.txt","r").read().split("\n")
        out=open("output.txt", "w")
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        total=len(f)
        
        
        for line in f:
            wordList=line.split()
            x1=self.parity(wordList[0])
            x2=self.palindrome(wordList[1])
            out.write(x1+x2+"\n")
            
        r=open("record.txt", "w")
        odd_parity=(self.b/total)*100
        
        print("Percentage of odd parity:",int(odd_parity),"%",file=r)
        
        even_parity=(self.c/total)*100
        print("Percentage of even parity:",int(even_parity),"%",file=r)
        
        no_parity=(self.a/total)*100
        print("Percentage of no parity:",int(no_parity),"%",file=r)
        
        pal=(self.d/total)*100
        print("Percentage of palindrome:",int(pal),"%",file=r)
        
        no_palindrome=100-pal
        print("Percentage of non-palindrome:",int(no_palindrome),"%",file=r)
        
        out.close()
        r.close()
    
    def parity(self,n):
    
        if "." in n:
            self.a+=1
            x=n + " cannot have parity and"
            return x
        else:
            y=int(n)
            if y%2==1:
                self.b+=1
                x=str(y)+" has odd parity and"
                return x
            else:
                self.c+=1
                x=str(y)+" has even parity and"
                return x
    
    def palindrome(self,word):
        n=len(word)
        if n==0:
            
            x=" "+ word + " is not a palindrome"
            return x
        for i in range(0,n//2):
            
            if word[i] != word[n-1-i]:
                x=" "+ word + " is not a palindrome"
                return x
        self.d+=1
        x= " "+ word + " is a palindrome"
        return x
percentage()


