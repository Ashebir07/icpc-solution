import sys
from math import gcd
def lcm_two(a,b):
    return a*b//gcd(a,b)

def lcm(x):
    try:
        a = next(x)
        b = next(x)
        y = lcm_two(a,b)
    except StopIteration:
        return a
    while True:
        try:
           y = lcm_two(y, next(x))
        except StopIteration:
            return y
def main():
    for i in sys.stdin:
        print(lcm(map(int, i.split())))


main()
