n=int(input())
l=[]
s=[]
for i in range(n):
    s=input()
    l.append(s)
for i in range(len(l)):
    if "DU"  in l[i]:
            x=l[i].count("U")-1
            print(x)
            
    else:
        x=l[i].count("U")
        print(x)
        
    
    
    
    
          
    

