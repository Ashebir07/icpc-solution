n=int(input())
for i in range(n):
    g,c,e=(int(i) for i in input().split())
    if e>c:
        x=e-c
        if g==1:
            print(int(x)*1)
        elif g==2:
            print(int(x)*3)
        elif g==3:
            print(int(x)*5)
    else:
        print(0)
