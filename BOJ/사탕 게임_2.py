import sys

input = sys.stdin.readline

n = int(input()) # 보드의 크기
board = [list(input()) for _ in range(n)]
maxCnt = 0

def count_candy():
    global maxCnt
    for i in range(n):
        cnt = 1 # 행을 검사
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 1
                
        cnt = 1 # 열을 검사
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 1
                
for i in range(n):
    for j in range(n):
        # 오른쪽과 바꿈
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            count_candy()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
        # 아래쪽과 바꿈
        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            count_candy()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            
print(maxCnt)