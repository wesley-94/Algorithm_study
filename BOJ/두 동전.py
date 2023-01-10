from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# BFS 함수 
def bfs():
    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        
        # 버튼을 10번 보다 많이 눌러야 하는 경우
        if cnt >= 10:
            return -1
        
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                # 벽인 경우 그대로 유지
                if board[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                q.append((nx1, ny1, nx2, ny2, cnt + 1)) # 버튼 누른 횟수 증가
            # coin2 가 떨어진 경우 end
            elif 0 <= nx1 < n and 0 <= ny1 < m:
                return cnt + 1
            # coin1 가 떨어진 경우 end
            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return cnt + 1
            # 둘 다 떨어진 경우 무시
            else:
                continue
            
# 데이터 입력 받기
n, m = map(int, input().split()) # n: 세로 크기 / m: 가로 크기
q = deque()
board = []
start = []

for i in range(n):
    board.append(list(input().strip()))
    for j in range(m):
        if board[i][j] == "o":
            start.append((i, j))
            
q.append((start[0][0], start[0][1], start[1][0], start[1][1], 0))

print(bfs())