N, x = map(int, input().split())

data = list(map(int, input().split()))

# 선형 탐색으로 해결 (문제에서 요구한 것은 이진 탐색)
cnt = 0
for item in data:
    if item == x:
        cnt += 1

if cnt == 0:
    print(-1)
else:
    print(cnt)