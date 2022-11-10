from itertools import combinations
import sys

n, k = map(int, input().split()) # 단어의 갯수

teached = {"a", "n", "t", "i", "c"}
remain_alpha = set(chr(i) for i in range(97, 97+26)) - teached

data = []
# original = []
for i in range(n):
    originalData = sys.stdin.readline().rstrip()
    # original.append(originalData)
    data.append(originalData[4:-4])
    

def checkReadData(data, learned):
    count = 0
    for origin in data:
        canRead = True
        for chr in origin:
            if learned[ord(chr)] == 0:
                canRead = False
                break
        if canRead == True:
            count += 1
    return count
        

result = []
if k >= 5:
    learned = [0] * 123 # 리스트 초기화
    
    for item in teached:
        learned[ord(item)] = 1
        
    # 남은 알파벳 중에서 k-5 개를 선택한다
    for teach in list(combinations(remain_alpha, k-5)):
        # print(teach)
        for alpha in teach:
            learned[ord(alpha)] = 1
        
        result.append(checkReadData(data, learned))
        
        # 초기화
        for alpha in teach:
            learned[ord(alpha)] = 0

    print(max(result))
else:
    print(0)