##from math import gcd
##a,b,c=map(int,input().split())
##gc=gcd(b*a,c-b)
##print(str(int((a*b)/gc))+"/"+str(int((c-b)/gc)))

while True:
    
    try:
        tc=int(input())
        if tc==0:
            break
        else:
            mls=[]
            
            for i in range(tc):
                inx=0
                k=1
                a=["A","B","C","D","E"]
                y=[int(i) for i in input().split()]
                for i in range(len(y)):
                    if y[i]<=127:
                        inx=i
                        k+=1

                        
                if k>2 or k==1:
                    mls.append("*")
                else:
                    mls.append(a[inx])
            for i in mls:
                print(i)
    except:
        break
        

