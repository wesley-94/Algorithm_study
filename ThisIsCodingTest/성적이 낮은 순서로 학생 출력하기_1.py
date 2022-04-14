n = int(input())
array = []
for i in range(n):
    data = input().split()
    array.append(data)
    
for j in range(len(array)):
    min_index = j
    for k in range(j+1, len(array)):
        if int(array[k][1]) < int(array[min_index][1]):
            array[k], array[min_index] = array[min_index], array[k]
            min_index = k
            
for item in array:
    print(item[0], end=' ')