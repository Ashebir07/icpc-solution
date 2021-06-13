import sys
adrian = ['A', 'B', 'C']
bruno = ['B', 'A', 'B', 'C']
goran = ['C', 'C', 'A', 'A', 'B', 'B']
n = int(input())
q = sys.stdin.readline().rstrip()
ds= {'Adrian': 0, 'Bruno': 0, 'Goran': 0}
for i in range(n):
    if q[i] == adrian[i % 3]:
        ds['Adrian'] += 1
    if q[i] == bruno[i % 4]:
        ds['Bruno'] += 1
    if q[i] == goran[i % 6]:
        ds['Goran'] += 1

max = 0
for key in ds.keys():
    if ds[key] > max:
        max = ds[key]

print(str(max))
for key in ds.keys():
    if ds[key] == max:
        print(key)
