import sys
input = sys.stdin.read()
line = input.strip("\n")
n = line.split()

new_numbers = []
different = False

n = sorted([int(x) for x in n])
diffs = []

for i in range(len(n)):
    if i < len(n) - 1:
        diff_new = n[i+1] - n[i]
        diffs.append(diff_new)

if len(set(diffs)) == 1:
    print (n[-1] + diffs[0])  
else:
    diff = max(diffs)
    for i in range(len(n)):
        if i < len(n) - 1:
            diff_new = n[i+1] - n[i]
            if diff == diff_new:
                print (n[i] + min(diffs))
