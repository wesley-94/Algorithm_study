n = int(input())
current = 0
result = 0
while True:
    current += 1
    
    if current == 1 or current % 2 == 0 or current % 3 == 0 or current % 5 == 0:
        result += 1
    
    if result == n:
        break
    
print(current)