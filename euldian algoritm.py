from math import  gcd
while True:
        try:
           def contest (a,b):
                   if a == 0 :
                           return b, 0, 1
                   gcd, x1, y1 =contest(b%a,a)
                   x = y1 - (b//a) * x1
                   y = x1
                   return gcd, x, y

           a, b = (int(i) for i in input().split())
           z, x, y = contest(a, b)
           print(z,(a*b//gcd(a,b)))
        except:
                break








