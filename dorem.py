import math
n=int(input())
for i in range(n):
    a,b,c=(int(i) for i in  input().split())
    print(b*c//(math.gcd((b*c),a)),a//(math.gcd((b*c),a)))
