h, w = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(1, w-1):
    left_max = max(data[:i])
    right_max = max(data[i+1:])
    
    compare = min(left_max, right_max)
    
    if data[i] < compare:
        result += (compare - data[i])
        
print(result)