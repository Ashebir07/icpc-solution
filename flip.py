x,y =(int(i) for i in input().split())
x=int(((x%10)*100))+int(((x/10)%10)*10)+int(((x/100)%10))
y=int(((y%10)*100))+int(((y/10)%10)*10)+int(((y/100)%10))
if x<y:
    print(y)
else:
    print(x)
