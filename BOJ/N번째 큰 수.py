T = int(input())

for i in range(T):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    print(data[2])