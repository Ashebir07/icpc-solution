from math import gcd
n=int (input())
for k in range(n):
    l=[]
    g=[]
    if n%2==0 and n>3:
        a=[int (i) for i in input().split()]
        for i in range(0,len(a),2):
            l.append([a[i],a[i+1]])
        for i in a:
            x=gcd(a[0],a[1])
            y=int(a[0]/x)
            z=int(a[1]/x)
            print(str(y)+"/"+str(z))

  
