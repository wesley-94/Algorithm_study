from itertools import combinations # 조합 라이브러리 사용

data = []
for i in range(9):
    item = int(input())
    data.append(item)
    
combinationList = list(combinations(data, 7))
for combination in combinationList:
    sum_value = sum(combination)
    if sum_value == 100:
        combination = sorted(combination) # 튜플 정렬
        for tupleitem in combination:
            print(tupleitem)
        break