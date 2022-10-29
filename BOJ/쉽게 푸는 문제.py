A, B = map(int, input().split())

number = 1
count = 1
data = []
for i in range(1, 1000+1):
    data.append(number)
    if number == count:
        number += 1
        count = 1
    else:
        count += 1
        
print(sum(data[A-1:B]))