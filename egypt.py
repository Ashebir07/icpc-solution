from math import *
while True:
    try:
        a,b,c=[int (i) for i in input ().split()]
        l=[]
        l.append(a)
        l.append(b)
        l.append(c)
        k=sorted(l)
        if(not (a==0 or b==0 or c==0)):
            if(k[0]**2+k[1]**2==k[2]**2):
                print ("right")
            else:
                print("wrong")
    except:
        break
    

