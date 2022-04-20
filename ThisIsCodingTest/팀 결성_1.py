def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

# 부모 테이블 초기화
for i in range(1, n+1):
    parent[i] = i

result = []

for i in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:
        union_parent(parent, a, b)
    else:
        a_find = find_parent(parent, a)
        b_find = find_parent(parent, b)
        if a_find == b_find:
            result.append("YES")
        else:
            result.append("NO")
            
# 결과 출력
for item in result:
    print(item)