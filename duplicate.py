n=int(input())
l=[str(i) for i in input().split()]
count=0
for i in range(n):
    x=l[i].upper()
    if l[i]==l[n-i-1]:
        count +=1
if count >1:
    print("no")
else:
    print("yes")
        
        
        

