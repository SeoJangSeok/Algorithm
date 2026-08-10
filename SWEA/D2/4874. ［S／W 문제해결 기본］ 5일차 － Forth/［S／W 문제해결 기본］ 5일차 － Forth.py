T = int(input())

for test_case in range(1, T + 1):
    forth = input().split()
    stack = []
    result = None
    
    for token in forth:
        if token.isdigit():
            stack.append(int(token))
            
        elif token in ['+', '-', '*', '/']:
            if len(stack) < 2:
                result = 'error'
                break
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
                
        elif token == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
            break
        
        else:
            result = 'error'
            break
        
    print(f'#{test_case} {result}')