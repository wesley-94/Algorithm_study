# 바이너리 인덱스 트리 (Binary Index Tree, BIT, 펜윅 트리)

# 데이터 업데이트가 가능한 상황에서의 구간 합 (Interval Sum) 문제

# 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다.
# 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지의 합을 구하라고 한다면 17을 출력하면 되는 것이다.
# 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지의 합을 구하라고 한다면 12가 될 것이다.

# 데이터 개수: N ( 1<= N <= 1,000,000 )
# 데이터 변경 횟수: M ( 1 <= M <= 10,000 )
# 구간 합 계산 횟수: K ( 1<= K <= 10,000 )

import sys
input = sys.stdin.readline

# 데이터의 개수(n), 변경 횟수(m), 구간 합 계산 횟수(k)
n, m, k = map(int, input().split())

# 전체 데이터의 개수는 최대 1,000,000개
arr = [0] * (n+1)
tree = [0] * (n+1)

# i번째 수까지의 누적 합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0 이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result

# i번째 수를 dif 만큼 더하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

# start 부터 end 까지의 구간 합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)

for i in range(m+k):
    a, b, c = map(int, input().split())
    # 업데이트(update) 연산인 경우
    if a == 1:
        update(b, c - arr[b]) # 바뀐 크기(dif)만큼 적용
        arr[b] = c
    # 구간 합(interval sum) 연산인 경우
    else:
        print(interval_sum(b, c))