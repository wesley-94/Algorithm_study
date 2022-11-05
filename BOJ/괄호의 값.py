data = list(input())

stack = []
result = 0
temp = 1

for i in range(len(data)):
    if data[i] == "(":
        stack.append(data[i])
        temp *= 2
        
    elif data[i] == "[":
        stack.append(data[i])
        temp *= 3
        
    elif data[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if data[i-1] == "(":
            result += temp
        stack.pop()
        temp //= 2
    
    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        if data[i-1] == "[":
            result += temp
        stack.pop()
        temp //= 3
        
if stack:
    print(0)
else:
    print(result)