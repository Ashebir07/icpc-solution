from math import sqrt
from math import ceil
n=0
while 1:
    try:
        
        x=int(input())
        if x==0:
            break
        else:
            
            y=ceil((3+sqrt(9+8*x))/2)
            n=n+1
            print("Case "+str(n)+": "+str(y))
        
    except:
        break
