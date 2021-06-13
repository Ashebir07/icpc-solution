import math
n, w, h = [int(i) for i in input().split()]
ans = math.sqrt(w*w + h*h) + 0.01

for i in range(n):
    if int(input()) < ans:
        print('DA')
    else:
        print('NE')
