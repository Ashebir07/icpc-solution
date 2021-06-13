t=int(input())
for i in range(t):
    a,b=[str(i) for i in input().split()]
    y=a[:1].lower()
    f=b.lower()
    x=str(y)+f+"@mapcom-group.com"
    print(x)
