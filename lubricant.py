n=int(input())
print("Lumberjacks:")
y=[]
yy=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    l.sort()
    y=l.sort(reverse=True)
for i in range(len(l)):
    if l[i]<l[i+1]:
         print("Ordered")
    elif y[i]>y[i+1]:
         print("Ordered")
    else:
         print("Unordered")
    
