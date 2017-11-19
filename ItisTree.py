def root(i):
    while tree[i] != i:
        tree[i] = tree[tree[i]]
        i = tree[i]
    return i

def connected(i, j):
    return root(i) == root(j)

def connect(i, j):
    tree[root(i)] = root(j)

tree = []
vertices, edges = map(int, input().split())
if vertices != edges + 1:
    print("NO")
else:
    for i in range(0, vertices):
        tree.append(i)
    flag = 0
    for i in range(edges):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if not connected(u, v):
            connect(u, v)
        else:
            flag = 1
    if flag == 1:
        print("NO")
    else:
        print("YES")