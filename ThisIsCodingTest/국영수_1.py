N = int(input())

data = []
for i in range(N):
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    data.append([name, kor, eng, math])

print(data)  
    
# 정렬 조건
# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
result = sorted(data, key = lambda x : (-x[1], x[2], -x[3], x[0]))
    
for item in result:
    print(item[0])