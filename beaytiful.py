a=int(input())
b=0
c=0
for i in range(a):
    b+=i
    if b==a:
        c+=1
if c==1:
    print("YES\n")
else:
    print("NO\n")
