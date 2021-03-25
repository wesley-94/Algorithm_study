# 모험가 길드

# 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
# '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.

# 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는
# 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.

# 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다.
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.

# 예를 들어 N = 5이고, 각 모험가의 공포도가 다음과 같다고 가정합시다.
# 2 3 1 2 2
# 이 경우 그룹 1에 공포도가 1, 2, 3인 모험가를 한 명씩 넣고, 그룹 2에 공포도가 2인 남은 두 명을 넣게 되면
# 총 2개의 그룹을 만들 수 있습니다.
# 또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에,
# 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.


# 나의 풀이

fear_list = input().split()
for k in range(len(fear_list)):
    fear_list[k] = int(fear_list[k])

item_list = sorted(fear_list, reverse=True)
print(item_list)

total = len(item_list)
criterion = item_list[0]
group = 0

while 1:

    for idx in range(criterion):
        item_list.pop(0)

    total = total - criterion
    group += 1
    if len(item_list) != 0:
        criterion = item_list[0]
    else:
        break

print(group)


# 답안
data = list(map(int, input().split()))
data.sort # 오름차순

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for item in data: # 공포도를 낮은 것부터 하나씩 확인하여
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= item: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력