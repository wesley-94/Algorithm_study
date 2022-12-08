s = int(input()) # 자연수의 합

sum = 0
result = 0
for i in range(1, s+1):
    sum += i # 비교 값 구하기
    result += 1
    
    if sum > s:
        result -= 1
        break
    
print(result)