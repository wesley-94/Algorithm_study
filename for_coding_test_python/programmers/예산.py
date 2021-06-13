# 프로그래머스
# 서머코딩/윈터코딩(~2018)
# 예산

def solution(d, budget):
    count = 0
    for i in sorted(d):
        budget -= i
        if budget >= 0:
            count += 1
    return count