a,b,c=(int(i) for i in input().split())
if a>0 and a<10:
    print(((1/b)%c)%(b%c))
elif a==10:
    print(b%c)
else:
    print()
