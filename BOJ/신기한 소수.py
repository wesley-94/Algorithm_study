N = int(input()) # 자릿수

# 소수 판별
def isPrime(n):
    if n <= 1:
        return False
    # 제곱근 까지만 비교하면 됨
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0:
            return False
    return True

# DFS 개념 활용
def dfs(n):
    if len(str(n)) == N:
        print(n)
    else:
        # 끝자리가 짝수로 끝나면 소수가 될 수 없음
        for i in range(1, 10, 2):
            temp = n * 10 + i
            if isPrime(temp):
                dfs(temp)
          
# 1의 자리 값이 소수인 경우로 시작해서 DFS 활용      
for i in [2, 3, 5, 7]:
    dfs(i)