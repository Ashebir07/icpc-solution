y=int(input())
print(" \n")
l=[]
s=0
for i in range(y):
    n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
   # print(" \n")
    s +=l[i]
if s%n==0:
    print("YES")
else:
    print("NO")

        
