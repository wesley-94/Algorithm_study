n = int(input())
for i in range(n):
    data = bin(int(input()))[2:]
    for index, item in enumerate(data[::-1]):
        item = str(item)
        if item == '1':
            print(index, end=' ')