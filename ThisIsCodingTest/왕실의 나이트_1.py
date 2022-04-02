start = input()
start_x_origin = ord(start[0])-97+1
start_y_origin = int(start[1])

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

possible = 0

# 특정 위치에서 움직일 수 있는 최대 경우의 수: 8
for i in range(8):
    start_x = start_x_origin + dx[i]
    start_y = start_y_origin + dy[i]
    if 0 < start_x <= 8:
        if 0 < start_y <= 8:
            possible += 1

print(possible)