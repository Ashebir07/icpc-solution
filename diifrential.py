import numpy
x = [1,3,4,6,7,8]
y = [1,2,4,2,3,1]
dx = numpy.diff(x)
dy = numpy.diff(y)
d = dy/dx
print(d)
