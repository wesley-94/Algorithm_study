# 프로그래머스
# 2019 KAKAO BLIND RECRUITMENT
# 실패율

def solution(N, stages):
    # 실패율
    dic = {}
    allPlayer = len(stages)
    for i in range(1, N+1):
        notClearPlayer = stages.count(i)
        if allPlayer == 0:
            failRate = 0
        else:
            failRate = notClearPlayer / allPlayer
        dic[i] = failRate

        allPlayer -= notClearPlayer

    # 실패율을 정렬
    dicSort = sorted(dic.items(), key = lambda x: x[1], reverse=True)

    # 정렬된 실패율 반환
    result = [dicSort[i][0] for i in range(len(dicSort))]
    return result