# 프로그래머스
# 2020 카카오 인턴십
# 수식 최대화

import re
import itertools
def solution(expression):
    operators = list(itertools.permutations(['-', '+', '*'], 3))
    expression = re.split('([-+*])', expression)
    
    results = []
    for operator in operators:
        exp = expression[:]
        for op in operator: # ['-', '+', '*']
            while op in exp:
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1] + op + exp[idx+1]))
                del exp[idx:idx+2]
        results.append(abs(int(exp[0])))
    return max(results)