from collections import deque

T = int(input())

while T:
    K, M, P = map(int, input().split()) # M: 노드 갯수 / P: 간선 갯수
    arr = [[] for _ in range(M + 1)]
    indegree = [0] * (M + 1) # 차수
    count = [[0, 0]] * (M + 1) # [값, 갯수] 의 배열
    order = [0] * (M + 1)
    queue = deque()
    
    for i in range(P):
        first, second = map(int, input().split())
        arr[first].append(second)
        indegree[second] += 1
        
    for i in range(1, M + 1):
        if indegree[i] == 0:
            count[i] = [1, 1]
            queue.append(i)
            
    while queue:
        temp = queue.popleft()
        
        if count[temp][1] >= 2: # 개수를 비교하여 값을 갱신 한다
            order[temp] = count[temp][0] + 1
        else:
            order[temp] = count[temp][0]
            
        for second in arr[temp]:
            indegree[second] -= 1
            if count[second][0] == order[temp]: # 같으면 개수 증가
                count[second][1] += 1
            elif count[second][0] < order[temp]: # 이번에 들어오는 값이 더 크다면 바꿔줌
                count[second] = [order[temp], 1]
                
            if indegree[second] == 0: # 0 이 됐을 때가 모든 값을 다 처리했을 때이므로, 큐에 넣어서 order 값을 갱신할 수 있도록 한다
                queue.append(second)
                
    print(K, order[M], end=" ")
    T -= 1