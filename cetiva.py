import sys
inputstd = sys.stdin.read()
line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]
p= []
for i in values:
	i= i.split()
	p.append(i)
	
x = []
y= []
for i in p:
	x.append(i[0])
	y.append(i[1])
	
r = ""
if x.count(x[0]) == 1:
	r += x[0] + " "
else:
	if x[0] != x[1]:
		r += x[1] + " "
	else:
		r += x[2] + " "
	

if y.count(y[0]) == 1:
	r += y[0]
else:
	if y[0] != y[1]:
		r += y[1]
	else:
		r += y[2]
		
print (r)
