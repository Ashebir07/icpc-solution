import math
def ring( x,y):
    for i in range(2,i<=x and i<=y):
        if x%i==0 and y%i==0:
            x /=i
            y /=i

n=int(input())
n-=1
f=[]
c=int(input())
for i in range(n):
    z=int(input())
    f.append(c)
    print(str(f)+"/"+str(z))
ring(f,z)  
            
