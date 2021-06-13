n=int(input())
l=[]
m=[]
xx=[]
s=0
tot=0
l=[int(i) for i in input().split()]
m=[str(i) for i in input().split()]
for i in range(len(m)):
    xx.append(m[i].replace("Birr"," "))
    s+=l[i]
    tot=tot+int(l[i])*int(xx[i])
    #print(xx[i])
print(str(s)+", "+str(tot))
