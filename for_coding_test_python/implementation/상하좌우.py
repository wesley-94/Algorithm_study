# 상하좌우

# 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있습니다.
# 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있습니다.
# 가장 왼쪽 위 좌표는 (1, 1)이며 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다.
# 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.

# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여
# L, R, U, D 중 하나의 문자가 반복적으로 적혀 있습니다.

# 각 문자의 의미는 다음과 같습니다.
# L: 왼쪽으로 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위로 한 칸 이동
# D: 아래로 한 칸 이동

# 이때 여행가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다.
# 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시됩니다.

# 입력 조건
# > 첫째 줄에 공간의 크기를 나타내는 N이 주어집니다.
# > 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다.
# 예시
# 5
# R R R U D D

# 출력 조건
# > 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백을 기준으로 구분하여 출력합니다.
# 예시
# 3 4


# 나의 답안

space = int(input())
move = list(map(str, input().split()))

X = 1
Y = 1

for item in move:
    if item == 'L' and X != 1:
        X -= 1
    if item == 'R' and X != space:
        X += 1
    if item == 'U' and Y != 1:
        Y -= 1
    if item == 'D' and Y != space:
        Y += 1

print('%d %s' % (X, Y))


# 답안 예시

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)