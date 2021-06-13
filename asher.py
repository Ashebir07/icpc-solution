E=[]
O=[]
T=[]
W=[]
S=[]
N,H=(int(i) for i in input().split())
for k in range(N):
    T.append(int(input()))
for j in range(N):
    if(j%2==0):
        E.append(T[j])
    else:
        O.append(T[j])
W.append(len(E))
for b in range(2,H+1):
    for a in range(int(N/2)):
        if(E[a]>=b and O[a]>=H-b+1):
            S.append(E[a])
            S.append(E[a])
        elif(E[a]>=b and O[a]<H-b+1):
            S.append(E[a])
        elif(E[a]<b and O[a]>=H-b+1):
            S.append(O[a])
    x=len(S)
    S.clear()
    W.append(x)
print(min(W),W.count(min(W)))

