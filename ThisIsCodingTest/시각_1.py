n = int(input())
n = n + 1
total = n * 60 * 60
# 3 이 들어가는 시각: 03, 13, 23 (총 3개)
# 3 이 들어가는 분, 초: 03, 13, 23, 30-39(10개), 43, 53 (총 15개)
if n < 3:
    case = 3 * 45 * 45
elif n < 13:
    case = (n-1) * 45 * 45
elif n < 23:
    case = (n-2) * 45 * 45
else:
    case = (n-3) * 45 * 45

total = total - case
print(total)