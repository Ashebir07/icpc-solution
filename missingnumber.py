n = int(input())
s= False
next = 1
for i in range(n):
    x = int(input())
    for j in range(next, x):
        print(j)
        s= True
    next = x + 1

if not s:
    print('good job')
