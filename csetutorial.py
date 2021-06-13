import sys
x= []
y = []
for i in range(int(input())):
	a, b = input().split()
	if len(x) < 12 and a not in x:
		s = a + " " + b
		x.append(s)
		y.append(a)
print('\n'.join(y))
