L=[]
H=[]
x=[str(i) for i in input().split()]
for i in range(9):
    L.append(x[i])

H.append(L[0])
H.append(L[1])
del (L[0])
del (L[0])
L.sort()
del L[-1]
del L[-1]
L.append(H[0])
L.append(H[1])
Sum=0
for i in range(7):
    if(L[i]=="A"):
        Sum+=4
    elif(L[i]=="B"):
        Sum+=3
    elif(L[i]=="C"):
        Sum+=2
    elif(L[i]=="D"):
        Sum+=1
    else:
        Sum+=0
gpa=Sum/7
print("%.2f"%gpa)
