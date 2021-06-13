array=list(map(int,input().split()))
ar_sorted =  sorted(array, key=int)
string = input()
if string == 'ABC':
    print(ar_sorted)
