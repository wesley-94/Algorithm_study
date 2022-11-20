from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input()) # 도시의 갯수
m = int(input()) # 버스의 갯수
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 c 라는 의미
    graph[a].append((b, c))
    
# 출발점의 도시 번호와 도착점의 도시 번호
start, end = map(int, input().split())

def dijkstra(start):
    q = [(0, start)]
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    
    while q:
        dist, now = heappop(q)
        if distance[now] < dist: # 이미 처리 되었다면 PASS
            continue
        
        for node, value in graph[now]:
            cost = distance[now] + value
            if cost < distance[node]:
                distance[node] = cost
                heappush(q, (cost, node))
                
# 다익스트라 알고리즘 수행
dijkstra(start)

# 최소 비용 출력
print(distance[end])