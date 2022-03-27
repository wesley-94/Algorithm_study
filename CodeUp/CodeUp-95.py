h, w = input().split()
h = int(h)
w = int(w)
n = int(input())
t = []
for a in range(h):
    t.append([])
    for b in range(w):
        t[a].append(0)
for i in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    if x > 100-h:
        x = 100-h
    if y > 100-w:
        y = 100-w
    if d == 0:
        for j in range(l):
            t[y-1][x-1+j] = 1
    else:
        for j in range(l):
            t[x-1+j][y-1] = 1
    print(t)
for k in range(h):
    for m in range(w):
        print(t[k][m], end=" ")
    print(" ")