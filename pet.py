l=[]
for i in range(5):
    x,y,z,w=(int (i) for i in input().split())
    l.append(x+y+z+w)
print(l.index(max(l))+1,max(l))
    
    
