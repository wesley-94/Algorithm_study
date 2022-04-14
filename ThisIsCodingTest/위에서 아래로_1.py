n = int(input())
array = []
for i in range(n):
    data = int(input())
    array.append(data)
    
array.sort(reverse=True)

for j in range(len(array)):
    print(array[j], end=' ')