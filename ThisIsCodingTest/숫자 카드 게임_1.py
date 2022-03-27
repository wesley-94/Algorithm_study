n, m = map(int, input().split())
max = 0
for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    first = data[0]
    if max <= first:
        max = first
        
print(max)