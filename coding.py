x1=input()
x2=input()
x3=input()
l = [x1,x2,x3]
for i in reversed(sorted(l,key=len,reverse=True)):
    print (i)
    
