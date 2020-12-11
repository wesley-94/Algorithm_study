from stack import Stack

def reverse_string_with_stack(str1):
    s = Stack()
    revStr = ''

    for c in str1:
        s.push(c)

    while not s.isEmpty():
        revStr += s.pop()

    return revStr

if __name__ == "__main__":
    str1 = '버피는 천사다.'
    print(str1)
    print(reverse_string_with_stack(str1))