a,b,c=[int(i) for i in input().split()]
if (a+b==c):
    print(str(a)+ "+"+str(b)+"="+str(c))
elif(a-b==c):
     print(str(a)+ "-"+str(b)+"="+str(c))
elif(a*b==c):
     print(str(a)+ "*"+str(b)+"="+str(c))    
    
elif(a==b-c):
     print(str(a)+"="+str(b)+"-"+str(c))
elif(a==b*c):
     print(str(a)+ "="+str(b)+"*"+str(c))
else:
    print(str(a)+"="+str(b)+"/"+str(c))
