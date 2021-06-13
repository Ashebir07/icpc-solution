y=False
n=int(input())
z=1
for i in range(n):
    x=int(input())
    for j in range(z,x):
        print(j)
        y=True
    z=x+1
if not y:
    print("good job")
