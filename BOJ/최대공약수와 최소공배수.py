x, y = map(int, input().split())
moreVal = max(x, y)

gong = 0
for i in range(1, moreVal+1):
    if x % i == 0 and y % i == 0:
        gong = i

yak = (x // gong) * (y // gong) * gong

print(gong)
print(yak)