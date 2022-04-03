## 미완성 코드 ##

n, m = list(map(int, input().split()))
start_x, start_y, direction = list(map(int, input().split()))

# 맵의 외곽은 항상 바다로 되어 있기 때문에, 
# (1, 1), (1, 2), (2, 1) 은 항상 바다일 수 밖에 없다.
# 바로 (2, 2)가 육지인지, 바다인지 체크해야 함

# direction 순서: 
# 3 -> 2 -> 1 -> 0
# direction_list = [3, 2, 1, 0]

walkCnt = 0
breakFlag = 0
whileCnt = 0

total_data = []
for i in range(n):
    data = list(map(int, input().split()))
    total_data.append(data)

for i in range(n):
    # 출발점 확인
    if i >= 1:
        if breakFlag == 0:
            for j in range(1, m+1):
                if total_data[i][j] == 0:
                    start_x = start_x + j
                    breakFlag = 1
                    break
                else:
                    pass
        else:
            pass
        
    if breakFlag == 0:
        start_y = start_y + 1
        
total_data[start_x-1][start_y-1] = 1
walkCnt += 1

# startCnt = 0
while True:
    
    walkTemp = 0
    # directionTemp = direction
    
    for i in range(4):
        if direction == 0:
            
            if total_data[start_x-1-1][start_y-1] == 0:
                total_data[start_x-1-1][start_y-1] = 1
                start_x = start_x - 1
                walkCnt += 1
                walkTemp += 1
                break
            else:
                direction = 3
            
        
        if direction == 1:
            
            if total_data[start_x-1][start_y+1-1] == 0:
                total_data[start_x-1][start_y+1-1] = 1
                start_y = start_y + 1
                walkCnt += 1
                walkTemp += 1
                break
            else:
                direction = 0
            
            
        if direction == 2:
            
            if total_data[start_x+1-1][start_y-1] == 0:
                total_data[start_x+1-1][start_y-1] = 1
                start_x = start_x + 1
                walkCnt += 1
                walkTemp += 1
                break
            else:
                direction = 1 
            
        
        if direction == 3:
            
            if total_data[start_x-1][start_y-1-1] == 0:
                total_data[start_x-1][start_y-1-1] = 1
                start_y = start_y - 1
                walkCnt += 1
                walkTemp += 1
                break
            else:
                direction = 2
            
    if walkTemp == 0:
        if direction == 0:
            start_y = start_y - 1
        elif direction == 1:
            start_x = start_x - 1
        elif direction == 2:
            start_y = start_y + 1
        else:
            start_x = start_x + 1
            
                
    whileCnt += 1
    # print(total_data)
    
    # while 문 탈출 조건
    # 변경 필요한 상태 
    
    checkCnt = 0
    for a in range(n):
        for b in range(m):
            if total_data[a][b] == 1:
                checkCnt += 1
                
    if checkCnt == n * m:
        break
    
    # if walkTemp == 0:
    #     break
    
print(walkCnt)