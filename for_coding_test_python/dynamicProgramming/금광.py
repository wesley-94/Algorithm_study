# 금광

# N X M 크기의 금광이 있습니다. 금광은 1 X 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.

# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
# 이후에 M-1 번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

# 입력 조건
# 첫째 줄에 테스트 케이스 T가 입력됩니다.
# 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. ( 1<=n, m<=20 )
# 둘째 줄에 n x m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. ( 1<= 각 위치에 매장된 금의 개수 <= 100 )

# 입력 예시
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

# 출력 예시
# 19
# 16

# 나의 답안


T = int(input())
hor_ver_list = []
array_total = []

# 리스트 원소 개수별로 나누기
def list_chunk(list_name, number):
    return [list_name[i:i+number] for i in range(0, len(list_name), number)]

result_list = []
for i in range(T):
    n, m = map(int, input().split())
    hor_ver_list.append([n,m])
    array = list(map(int, input().split()))
    array_total.append(array)
    check_list = list_chunk(array_total[i], hor_ver_list[i][1])
    # print(check_list)
    # 리스트 전치
    re_sort = [list(x) for x in zip(*check_list)]
    print(re_sort)
    # 케이스별 최댓값 구하기
    sum = 0
    for item in re_sort:
        sum += max(item)
    result_list.append(sum)

print('\n'.join(map(str, result_list)))


# 정답 안

# 문제 해결 아이디어
# 금광의 모든 위치에 대하여 다음의 세 가지만 고려하면 됩니다.
#   1. 왼쪽 위에서 오는 경우
#   2. 왼쪽 아래에서 오는 경우
#   3. 왼쪽에서 오는 경우
# 세 가지 경우 중에서 가장 많은 금을 가지고 있는 경우를 테이블에 갱신해주어 문제를 해결합니다.

# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
# 점화식:
#   dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
# 이 때 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크해야 합니다.
# 편의상 초기 데이터를 담는 변수 array 를 사용하지 않아도 됩니다.
#   바로 DP 테이블에 초기 데이터를 담아서 다이나믹 프로그래밍을 적용할 수 있습니다.

# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j]+ max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)