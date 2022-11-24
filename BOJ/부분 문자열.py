word = input()
pattern = input()

# KMP 알고리즘을 수행하기 전, 패턴을 처리하는 함수
# 패턴의 테이블 생성
def make_table(pattern):
    len_pattern = len(pattern)
    table = [0] * len_pattern # 정보 저장용 테이블
    
    pidx = 0 # 테이블의 값을 불러오고, 패턴의 인덱스에 접근
    for idx in range(1, len_pattern): # 테이블에 값을 저장하기 위해 활용하는 인덱스
        # pidx가 0이 되거나, idx와 pidx의 pattern 접근 값이 같아질 때까지 진행
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = table[pidx-1]
            
        # 값이 일치하는 경우, pidx를 1 증가시키고 그 값을 table에 저장
        if pattern[idx] == pattern[pidx]:
            pidx += 1
            table[idx] = pidx
            
    return table

def kmp(word, pattern):
    # KMP_table을 통해 전처리된 테이블 불러오기
    table = make_table(pattern)
    
    len_word = len(word)
    len_pattern = len(pattern)
    results = [] # 결과를 만족하는 인덱스 시점을 기록하는 리스트
    pidx = 0
    
    for idx in range(len_word):
        # 단어와 패턴이 일치하지 않는 경우, pidx를 table을 활용해 변경
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = table[pidx-1]
        # 해당 인덱스에서 값이 일치한다면, pidx를 1 증가시킴
        # 만약 pidx가 패턴의 끝까지 도달했다면, 시작 인덱스 값을 계산하여 추가 후 pidx 값 table의 인덱스에 접근하여 변경
        if word[idx] == pattern[pidx]:
            if pidx == len_pattern-1:
                return 1
            else:
                pidx += 1
                
    return 0

print(kmp(word, pattern))