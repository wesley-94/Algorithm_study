n, k = map(int, input().split()) # n : 멀티탭 갯수 / k : 전기용품의 총 사용 횟수
data = list(map(int, input().split()))

plugs = [0] * n

changeItem = 0
maximum = 0
result = 0

schedulingIdx = 0
for item in  data: # 리스트에서 삭제해 나가기 때문에, 탐색 대상의 데이터들만 남아있으므로, 0번째 데이터를 가져다 사용할 수 있는 것
    # 1. 멀티탭에 동일한 제품이 꽂혀 있다면 넘어감
    if item in plugs:
        pass
    
    # 2. 멀티탭에 빈자리가 있으면 해당 제품 꽂음
    elif 0 in plugs:
        plugs[plugs.index(0)] = item
        
    # 3. 멀티탭에 빈자리가 없을 때
    else:
        for plug in plugs:
            # 멀티탭에 꽂혀있는 제품 중 이후에 꽂는 제품이 없는 경우, 그 제품을 빼고 탐색 중인 제품을 꽂는다
            if plug not in data[schedulingIdx:]:
                changeItem = plug
                break
            # 멀티탭에 꽂혀있는 제품 중 가장 나중에 사용하는 제품을 골라 빼고 탐색 중인 제품을 꽂는다
            elif data[schedulingIdx:].index(plug) > maximum:
                maximum = data[schedulingIdx:].index(plug)
                changeItem = plug
        # 실제로 변경
        plugs[plugs.index(changeItem)] = item
        # 기준 값 리셋
        maximum = 0
        # 변경 값 증가
        result += 1
    # 다음 for문 준비
    schedulingIdx += 1
        
# 결과 값 출력
print(result)