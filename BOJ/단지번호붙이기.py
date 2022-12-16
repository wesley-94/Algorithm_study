from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    count = 1 # 시작 count
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    
    return count

n = int(input()) # 입력 값 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
count_of_house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count_of_house.append(bfs(graph, i, j))
            
# 정렬
count_of_house.sort()

# 값 출력
length = len(count_of_house)

print(length)
for i in range(length):
    print(count_of_house[i])