n = int(input())
data = input().split()
start_x = 1
start_y = 1

for item in data:
    if item == "L":
        start_y = start_y - 1
    elif item == "R":
        start_y = start_y + 1
    elif item == "U":
        start_x = start_x - 1
    else:
        start_x = start_x + 1
        
    if start_x == 0:
        start_x = start_x + 1
    if start_y == 0:
        start_y = start_y + 1
    if start_x == n:
        start_x = start_x - 1
    if start_y == n:
        start_y = start_y - 1

print(start_x, start_y, end= " ")