def fact(n):
    if n==1:
        return 1
    return (n*fact(n-1))
a=int(input())
for i in range(a):
    b=int(input())
    if fact(b%10)>10:
        print(0)
    else:
        print(fact(b%10))
    

