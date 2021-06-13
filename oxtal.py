b=input()
o=int(b,2)
x=oct(o)
y=""
for i in x:
    if i in "123456789":
        y+=i
print(y)
        
