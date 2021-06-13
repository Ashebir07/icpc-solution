n = int(input())
l= 0
while True:
    l += 1
    y = 2**((l-1)//2)
    if y>= n:
        pal = '1'
        s = ''
        if l > 2:
            s = bin(n-1)[2:].zfill((l-1)//2)
        b = pal + s + s[::-1] + pal
        if l % 2 == 1:
            b = b[:len(b)//2] + b[len(b)//2+1:]
        ans = int(b, 2)
        print(ans)
        break
    n -= y

