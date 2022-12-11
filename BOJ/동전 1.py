n, k = map(int, input().split()) # n: 동전의 종류 / k: 가치의 합
coin = [int(input()) for i in range(n)] # 코인의 종류
    
dp = [0 for i in range(k+1)] # dp 테이블 초기화
dp[0] = 1 # 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언

for i in coin:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
            
print(dp[k])