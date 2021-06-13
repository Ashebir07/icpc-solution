from math import gcd
while True:
    try:
        a,b=[int(i) for i in input().split()]
        x=gcd(a,b)
        print(int((a*b)/(x**2)))
    except:
        break
        
