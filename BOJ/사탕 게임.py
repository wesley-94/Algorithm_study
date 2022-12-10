# 최대 사탕 갯수 세기
def count_candy():
    row_cnt, col_cnt, row_max, col_max = 1, 1, -1e9, -1e9
    # 행 계산
    for i in range(n):
        for j in range(n-1):
            # 행 기준 동일한 색상이라면
            if board[i][j] == board[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_max, row_cnt)
        row_cnt = 1
    # 열 계산
    for j in range(n):
        for i in range(n-1):
            # 열 기준 동일한 색상이라면
            if board[i][j] == board[i+1][j]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_max, col_cnt)
        col_cnt = 1
    # 먹을 수 있는 최대 사탕 갯수 구하기
    answer = max(row_max, col_max)
    return answer

result = 0
n = int(input()) # 보드의 크기
board = [list(input()) for _ in range(n)]

# 상, 하, 좌, 우 방향
steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    for j in range(n):
        # 총 4가지 방향에 대하여
        for k in range(4):
            nx = i + steps[k][0]
            ny = j + steps[k][1]
            # 보드를 벗어나는 경우 제외
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 인접한 두 칸이 다른 색의 사탕인 경우
            if board[i][j] != board[nx][ny]:
                board[nx][ny], board[i][j] = board[i][j], board[nx][ny]
                # 이전의 사탕 개수와 비교하며 최댓값 계산
                result = max(result, count_candy())
                # 인접한 두 칸 원 위치
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
            
# 정답 출력        
print(result)