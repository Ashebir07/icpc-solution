from math import e
factorial = [ 1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200]
n = int(input())
print("%.12f" % (e if n>14 else sum(1/factorial[i] for i in range(n+1))))
