import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    dp[node][0], dp[node][1] = 0, 1
    
    for child in tree[node]:
        if not visited[child]:
            dfs(child) # 자식노드부터 처리한다.
            dp[node][0] += dp[child][1] # 자신이 얼리어댑터가 아닌 경우
            dp[node][1] += min(dp[child][0], dp[child][1]) # 자신이 얼리어댑터인 경우

n = int(input()) # 정점 갯수
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# dp[i][0] = 자신이 얼리어댑터가 아닌 경우에 필요한 친구의 수
# dp[i][1] = 자신이 얼리어댑터인 경우에 필요한 친구의 수
dp = [[0, 0] for _ in range(n + 1)]
visited = [False] * (n + 1)

dfs(1)
print(min(dp[1][0], dp[1][1]))