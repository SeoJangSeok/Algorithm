T = int(input())

for test_case in range(1, T + 1):
    stack = []
    code = input()
    result = 1
    
    for chr in code:
        if chr == '(' or chr == '{':
            stack.append(chr)
        elif chr == ')' or chr =='}':
            if not stack:
                result = 0
                break
            top = stack.pop()
            if (top == '(' and chr != ')') or (top =='{' and chr != '}'):
                result = 0
                break
    
    if stack:
        result = 0
    
    print(f'#{test_case} {result}')