import sys
from itertools import combinations

n = int(sys.stdin.readline())
result = []

# 반복문을 통해 감소하는 수 조합
# 최대 감소하는 수: 9876543210
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        result.append(int("".join(map(str, num))))
        
result.sort() # 감소하는 수 정렬
# 결과 값 출력
print(result[n] if len(result) > n else -1) # print 문에 if 문 사용 가능