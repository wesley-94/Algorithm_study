n, m, k = map(int, input().split()) # N, M, K 를 공백으로 구분하여 입력 받기
data = list(map(int, input().split())) # N 개의 수를 공백으로 구분하여 입력 받기

data.sort() # 데이터 오름차순 정렬

first = data[n-1] # 첫번째로 높은 수
second = data[n-2] # 두번째로 높은 수

size = m
sum = 0

while 1:
    for i in range(k): # 가장 큰 수를 K 번 더하기
        if m == 0:
            break
        sum += first
        m -= 1
        
    if m == 0:
        break
    
    sum += second # 두 번째로 큰 수 한 번 더하기
    m -= 1
    
print(sum)