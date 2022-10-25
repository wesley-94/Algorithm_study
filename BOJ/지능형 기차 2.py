result = 0
people = 0
for i in range(10):
    x, y = map(int, input().split()) # 내린 사람 수, 탄 사람 수
    people = people + (y - x)
    result = max(result, people)
    
print(result)