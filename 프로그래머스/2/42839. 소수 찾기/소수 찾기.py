def solution(numbers):
    numbers_combi = set()
    exist = [False] * len(numbers)
    
    # 가능한 조합의 숫자를 생성
    def dfs(current):
        if current:
            numbers_combi.add(int(current))
            
        for i in range(len(numbers)):
            if not exist[i]:
                exist[i] = True
                dfs(current + numbers[i])
                exist[i] = False
        
    def is_prime(number):
        if number < 2:
            return False
        
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                return False
        return True
    
    dfs('')
    
    answer = 0
    
    for number in numbers_combi:
        if is_prime(number):
            answer += 1
    return answer