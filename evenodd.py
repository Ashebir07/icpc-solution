n=int(input())
l=[int(i) for i in input().split()]
s=0
d=0
for i in range(n):
    if l[i]%2==0:
        s +=l[i]
    else:
        d+=l[i]
        
print (str(d)+" <=> "+str(s))
