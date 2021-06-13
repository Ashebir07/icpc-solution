n=int(input())
gpa=(float (i) for i in input().split())
x=sorted(gpa)
if len(x)%2!=0:
    ans=x[(len(x)//2)]
    print("%.2f"%ans)
else:
    ans = (x[(len(x)//2)]+x[(len(x)//2-1)])/2
    print("%.2f"%ans)

