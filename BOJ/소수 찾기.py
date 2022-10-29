N = int(input())
data = list(map(int, input().split()))

result = 0
for item in data:
    count = 0
    for i in range(1, item+1):
        if item % i == 0:
            count += 1
    
    if count == 2:
        result += 1
        
print(result)