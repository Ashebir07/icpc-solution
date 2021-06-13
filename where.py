n=int(input())
l=[]
for i in range(n):
    t=int(input())
    for i in range(t):
        x=input()
        l.append(set(x))
        j=set(int(len(l)) for i in range(t))
print(j)
    
