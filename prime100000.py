def s():
    prime=[True  for i in range(1000000)]
    p=2
    l=[]
    while (p * p <= 1000000):
        if(prime[p]==True):
            for i in range(p*p,1000000,p):
                prime[i]=False
        p+=1
    for i in range(2,1000000):
        if prime[i]:
            l.append(i)
    print(l)
s()
                
