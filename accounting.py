n,y=(int(i) for i in input().split())
l=[]
##for i in range(n):
##    y=input()
##    l.append(y)
for i in range(y):
    y=input()
    l.append(y)
    if "SET"  in l:
        a,b=(str(i) for i in input().split())
        t="SET"+" "+str(a)+" "+str(b)
        print(int(b))
    elif "PRINT" in l:
        x="PRINT"+" "+str(input())
        xz=x.remove("PRINT",end=" ")
        print(int(xz))
    elif "RESTART" in l:
        z="RESTART"+" "+str(input())
        zz=z.remove("RESTART",end=" ")
        print(zz)
            
        
            
		
    
