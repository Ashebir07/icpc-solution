a=int(input())
b=[]
for i in range(0,a):
    m=int(input())
    b.append(m%42)
print(len(set(b)))

