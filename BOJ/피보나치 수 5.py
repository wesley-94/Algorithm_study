n = int(input())
result_n = 0
for i in range(n+1):
    if i == 0:
        result_n_minus_2 = 0
        result_n = result_n_minus_2
    elif i == 1:
        result_n_minus_1 = 1
        result_n = result_n_minus_1
    else:
        result_n = result_n_minus_1 + result_n_minus_2
        result_n_minus_2 = result_n_minus_1
        result_n_minus_1 = result_n
        
print(result_n)