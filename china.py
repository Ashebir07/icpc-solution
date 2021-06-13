def china(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b%a
        m, n = x - u*q, y - v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

t = int(input())
for i in range(t):
    a, n, b, m = map(int, input().split())
    gcd, u, v = china(n, m)

    if abs(a-b) % gcd != 0:
        print('no solution')
        continue

    k = (n*m)//gcd 
    x = ((b-a)*u*n)//gcd + a
    print(x%k, k)
