b=[]
for i in range(10):
    m=int(input())
    b.append(m%42)
print(len(set(b)))
