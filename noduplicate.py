c=0
l=[str(i) for i in input().split()]
n=len(l)
for i in range(n):
    x=l[i].upper()
    if l[i]==l[n-i-1]:
        c +=1
if c>1:
    print("no")
else:
    print("yes")
