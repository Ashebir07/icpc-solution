t = int(input())
print("Lumberjacks:")
for i in range(t):
    x = [int(j) for j in input().split()]
    y = set(x)
    if len(x) != len(y):
        print('Unordered')
    elif x.sort() == x or x.sort(reverse=True) == x:
        print('Ordered')
    else:
        print('Unordered')
