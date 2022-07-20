N = input()
midIndex = len(N) // 2

left = N[0:midIndex]
right = N[midIndex:]

leftVal = 0
for item in left:
    leftItem = int(item)
    leftVal += leftItem
    
rightVal = 0
for itemTwo in right:
    rightItem = int(itemTwo)
    rightVal += rightItem
    
if leftVal == rightVal:
    print("LUCKY")
else:
    print("READY")