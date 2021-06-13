x=input()
y=input()
z=input()
l=[]
l.append(x)
l.append(y)
l.append(z)
x=sorted(l, key=lambda l: (len(l),l))
for i in range(len(l)):
    print(x[i])
