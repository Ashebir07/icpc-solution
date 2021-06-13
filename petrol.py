n=int(input())
l=[]
m=[]
s=0
a,b,c=(int(i) for i in input().split())
x,y,z=[str(i)for i in input().split("Birr")]
l.append(x)
l.append(y)
l.append(z)
#v=str(l.split("Birr"))
m.append(a)
m.append(b)
m.append(c)
for i in range(n):
    s+=l[i]*m[i]
print(str(a+b+c)+","+str(s))

