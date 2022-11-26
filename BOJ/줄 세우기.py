from collections import deque

n, m = map(int, input().split()) # n: 학생의 수 / m: 키를 비교한 횟수

graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
q = deque()
result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1 # 진입차수 1 증가
    
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i) # 큐에 삽입
        
while q:
    item = q.popleft()
    result.append(item)
    for i in graph[item]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)
            
print(*result)