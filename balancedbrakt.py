def check(y): 
    b = ['()', '{}', '[]'] 
    while any(i in y for i in b): 
        for i in b: 
            y = y.replace(i, '') 
    return not y 

n=int(input())
for i in range(n):
    s=input() 
    print("YES"
          if check(s) else "NO") 
