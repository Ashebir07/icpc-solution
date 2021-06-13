ja, ji= [int(i) for i in input().split()]
if ja==0 and ji==0:
    print("\n")
else:
    jack =set(int(input()) for i in range(ja))
    jill =set(int(input()) for i  in range(ji))
    x = jack and jill
    print(len(x)-1)


   
