l=[int(i) for i in input().split()]
s=input()
d={}
d[s[0]]=l[0]
d[s[1]]=l[1]
d[s[2]]=l[2]
y=sorted(d.keys())
for i in y:
    print(d[i],end=" ")
