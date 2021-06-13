n=int(input())
l=[]
s=0
for i in range(n):
    q,y=[float(i) for i in input().split()]
    if q >0 and q<=1:
        l.append(q*y)
for i in range(n):
    s+=l[i]
print("%.3f"%s)
    
