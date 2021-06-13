def vertices(i, edges):
    for j in edges[i]:
        if j != i:
            for k in edges[j]:
                if k != j and k != i and i in edges[k]:
                    return False
    return True


def contest(v):
    edges = {i: {j: None for j in map(lambda e: e[0], filter(lambda x: x[1] == "1", enumerate(input().split())))} for i in range(0, v)}
    weak = [i for i in filter(lambda j: v(j, edges), range(0, v))]
    for i in range(0, len(weak)):
        if i == len(weak) - 1:
            print(weak[i], end='')
        else:
            print(weak[i], end=' ')
    print()

while True:
    n = int(input())
    if n < 0:
        break
    contest(n)
