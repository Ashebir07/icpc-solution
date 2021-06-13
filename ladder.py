import math 
h,d=[int(i) for i in input().split()]
x=d*math.pi/180
l=int(math.ceil(h/math.sin(x)))
print(" "+str(l))
