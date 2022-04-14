n, k = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A.sort()
array_B.sort(reverse=True)

cnt = 0
start = 0
while 1:
    
    # 원소 바꿔치기
    if array_A[start] < array_B[start]:
        array_A[start], array_B[start] = array_B[start], array_A[start]
        cnt += 1
    
    if cnt >= k:
        break
    
    start += 1
    
sum = 0
for i in range(n):
    sum += array_A[i]

print(sum)