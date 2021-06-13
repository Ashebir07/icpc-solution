x = [1,1,2,2,2,8]
s = input()
y= s.split()
for i in range(0, 6):
    print(x[i] - int(y[i]), end=" ")
print()
