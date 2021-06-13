# 프로그래머스
# 탐욕법(Greedy)
# 체육복

def solution(n, lost, reserve):
    student = [1]*n
    for i in reserve:
        student[i-1] = 2
    for i in lost:
        student[i-1] = student[i-1] - 1

    for i,v in enumerate(student):
        if i > 0  and v == 0 and student[i-1] == 2:
            student[i] = 1
            student[i-1] = 1
        elif i < n-1 and v == 0 and student[i+1] == 2:
            student[i] = 1
            student[i+1] = 1

    return n-student.count(0)