# 줄 수에 대한 정보 입력 받기
n = int(input())

dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화
for i in range(n):
    array = list(map(int, input().split()))
    dp.append(array)
    
# 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
for i in range(1, n): 
    for j in range(i+1): 
        # 대각선 왼쪽에서 오는 경우
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i-1][j-1]
        # 대각선 오른쪽에서 오는 경우
        if j == i:
            right_up = 0
        else:
            right_up = dp[i-1][j]
        
        dp[i][j] = dp[i][j] + max(left_up, right_up)
        
print(max(dp[n-1]))