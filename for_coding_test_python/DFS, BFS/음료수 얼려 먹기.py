# 음료수 얼려 먹기

# N X M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.

# 다음의 4 X 5  얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.
# 00110
# 00011
# 11111
# 00000

# 입력 조건
# - 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1 <= N, M <= 1,000)
# - 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어집니다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000 

# 출력 조건
# 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.
# 출력 예시
# 3


# 나의 답안

# rowcol = list(map(int, input().split()))
# shape = ""
# for idx in range(2, rowcol[0]+1+1):
#     temp = input()
#     shape = shape + temp + "\n"

# # print(rowcol)
# # print(shape)

# connect = []

# shape_list = shape.split('\n')

# for item in shape_list:
#     for item_idx in range(len(item)):
#         connect.append(item[item_idx])


# 문제 해결 아이디어
# -> 얼음을 얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다고 표현할 수 있으므로
#    그래프 형태로 모델링 할 수 있음

# DFS를 활용하는 알고리즘
#   1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있따면 해당 지점을 방문함
#   2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
#   3. 모든 노드에 대하여 1~2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트함

# 정답안

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)