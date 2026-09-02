def is_valid(string):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            # 스택이 비어있거나 Top 괄호와 짝이 맞지 않는 경우
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop()
            
    # 모든 순회 후 스택이 비어 있어야 함
    return len(stack) == 0

def solution(s):
    answer = 0
    n = len(s)
    
    # s의 길이가 홀수이면 무조건 올바른 괄호가 안됨.
    if n % 2 != 0:
        return 0
    
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            answer += 1
    
    return answer