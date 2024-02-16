def parity(n):
    if "." in n:
        x=n + " can not have parity"
        return x
    else:
        y=int(n)
        if y%2==1:
            x=str(y)+" has odd parity"
            return x
        else:
            x=str(y)+" has even parity"
            return x
print(parity("3"))           
            
        

