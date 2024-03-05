from collections import deque

T = int(input()) # 테스트 케이스의 갯수

for _ in range(T):
    N, K = map(int, input().split()) # N : 건물의 갯수 / K : 건설순서 규칙의 총 갯수
    times = list(map(int, input().split())) # 각 건물 당 건설에 걸리는 시간
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1
        
    # 위상정렬 알고리즘 사용
    queue = deque()
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = times[i - 1]
            
    while queue:
        cur = queue.popleft()
        
        for next_node in graph[cur]:
            in_degree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[cur] + times[next_node - 1])
            
            if in_degree[next_node] == 0:
                queue.append(next_node)
            
    W = int(input())
    print(dp[W])