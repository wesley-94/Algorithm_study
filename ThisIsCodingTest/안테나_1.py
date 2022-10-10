n = int(input())
data = list(map(int, input().split()))
data.sort()

resultList = []
index = 0
index_min = 0
total_min = 100000
for i in data:
    total = 0
    for j in data:
        distance = abs(i-j)
        total += distance
    if total_min > total:
        total_min = total
        index_min = index
    index += 1    
    
print(data[index_min])