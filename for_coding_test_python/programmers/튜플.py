# 프로그래머스
# 2019 카카오 개발자 겨울 인턴십
# 튜플

def solution(s):
    nums = eval(s[1:-1])
    if len(nums) > 1:
        nums = sorted(nums, key=lambda n: sum(n))
    else:
        return list(nums)

    result = []
    for num in nums:
        for n in num:
            if n not in result:
                result.append(n)
    return result