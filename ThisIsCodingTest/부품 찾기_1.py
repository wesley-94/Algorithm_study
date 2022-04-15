# 이진 탐색 활용

n = int(input())
array_total = list(map(int, input().split()))
m = int(input())
array_search = list(map(int, input().split()))

array_total.sort() # 오름차순 정렬
array_search.sort()

# 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        # 중간 값
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result_list = []
for item in array_search:
    result = binary_search(array_total, item, 0, len(array_total)-1)
    if result is not None:
        result_list.append('yes')
    else:
        result_list.append('no')
        
for yesorno in result_list:
    print(yesorno, end=' ')