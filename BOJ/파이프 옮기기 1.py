import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ho = 0 # 가로
ver = 1 # 세로
diag = 2 # 대각선
count = 0 # 경우의 수

def dfs(x, y, type):
    global count
    if (x, y) == (n-1, n-1):
        count += 1
        return
    
    # 현재 위치가 가로 또는 대각선인 경우
    if type == ho or type == diag:
        if y+1 < n and board[x][y+1] == 0:
            dfs(x, y+1, ho)
            
    # 현재 위치가 세로 혹은 대각선인 경우
    if type == ver or type == diag:
        if x+1 < n and board[x+1][y] == 0:
            dfs(x+1, y, ver)
            
    if x+1 < n and y+1 < n:
        if board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
            dfs(x+1, y+1, diag)
            
# dfs 실행
dfs(0, 1, ho)
# 결과 값 출력
print(count)