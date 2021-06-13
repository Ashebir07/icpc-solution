#x,y,z=(int(i)for i in input().split())
while x!=0 and y!=0 and z!=0 :
    try:
        x,y,z=(int(i)for i in input().split())

        print(x*y*z)
    except:
        break
