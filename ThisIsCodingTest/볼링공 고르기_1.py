n, m = map(int, input().split())
data = list(map(int, input().split()))

case = 0 
for i in range(n):
    item_from = data[i]
    for j in range(i+1, n):
        item_to = data[j]
        if item_from != item_to:
            case += 1
            
print(case)