N, K = map(int, input().split())

check = 0
endFlag = "N"
for i in range(1, N+1):
    if N % i == 0:
        check += 1
        
    if check == K:
        endFlag = "Y"
        print(i)
        break
    
if endFlag == "N":
    print(0)