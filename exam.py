fs=int(input())
ma=input()
fa=input()
e=len(ma)
m=sum(a==b for a,b in zip(ma,fa))
if m>=fs:
    print(fs+(e-m))
else:
    print(m+(e-fs))
