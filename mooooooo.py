while True:
    try:
        a=[int(i) for i in input().split()]
        if len(a)==3:
            print((a[0]*a[1])%a[2])
        elif len(a)==2:
            print((a[1]%a[0])*(a[1]%a[0]))
        elif len(a)==1:
            print(" ")
    except:
        break

