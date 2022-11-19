n, s = map(int, input().split())
data = list(map(int, input().split()))

left, right = 0, 0 # 두 개의 포인터는 0 에서 시작
result = 0 # 합을 저장할 변수
min_value = int(1e9) # 최대 길이로 setting

while True:
    # 총 합이 S 가 넘는다면, left 를 줄이며 어디까지 줄일 수 있는지 확인
    if result >= s:
        min_value = min(min_value, right - left)
        result -= data[left]
        left += 1
    elif right == n:
        break
    # 총 합이 S 를 넘는다면, right 를 늘리며 총 합이 S 가 넘을 때까지 진행
    else:
        result += data[right]
        right += 1
        
if min_value == int(1e9):
    print(0)
else:
    print(min_value)