n=int(input())
a=[]
b=[]
for i in range(n):
    
    l,c=[i for i in input().split()]
    a.append([l,int(c)])
    #a.sort()
    b.append(int(c))
    y=b.index(max(b))
    z=b.index(min(b))
print(a[y][0])
print(a[z][0])

    
