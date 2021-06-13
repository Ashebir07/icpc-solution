l=[4,3,3,3,3,3]
d={"A":4,"B":3,"C":2,"D":1,"F":0}
x=input().split()
s=0
for i in range(len(l)):
    s+=l[i]*d[x[i]]
v=s/19
print("%.2f"%v)
