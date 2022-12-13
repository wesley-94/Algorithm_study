n, k = map(int, input().split()) # n: 동전의 종류 / k: 가치의 합
coins = [int(input()) for i in range(n)] # 코인의 종류

dp = [10001] * (k+1) # dp 테이블 초기화
dp[0] = 0 

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
        
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])