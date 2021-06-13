a,b,c=(int(i) for i in input().split())
l=[]
l.append(a)
l.append(b)
l.append(c)
l.sort()
x=l[2]-l[1]
y=l[1]-l[0]
if x>y:
    s=l[1]+l[1]-l[0]
elif x<y:
    s=l[0]+l[2]-l[1]
else:
    s=l[2]+l[2]-l[1]
print(s)
