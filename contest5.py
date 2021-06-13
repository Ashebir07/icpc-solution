n=int(input())
l=[]
c=[]
for i in range(n):
    a=[int(i) for i in input() ]
for i in range(len(a)):
    l.append(str(a[i]))
c.append(l[0]+l[1]+l[2]+l[3])
for i in range(n):
    if l.count(0)==a[0] or l.count(1)==a[1] or l.count(1)==a[2] or l.count(0)==a[3]:
        print("self-describing")
    else:
        print("not self-describing")
         
        
    




 
    
