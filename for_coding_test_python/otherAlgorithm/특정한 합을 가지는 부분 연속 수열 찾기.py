# 특정한 합을 가지는 부분 연속 수열 찾기

# N개의 자연수로 구성된 수열이 있습니다.
# 합이 M인 부분 연속 수열의 개수를 구해보세요.
# 수행 시간 제한은 O(N) 입니다.

# 문제 해결 아이디어

# 투 포인터를 활용하여 다음과 같은 알고리즘으로 문제를 해결할 수 있습니다.
#   1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
#   2. 현재 부분 합이 M과 같다면, 카운트한다.
#   3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다.
#   4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다.
#   5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start 를 차례대로 증가시키며 반복
for start in range(n):
    # end 를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)