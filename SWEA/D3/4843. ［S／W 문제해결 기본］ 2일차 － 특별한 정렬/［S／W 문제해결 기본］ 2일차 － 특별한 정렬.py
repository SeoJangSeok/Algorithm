T = int(input())

for test_case in range(1, T+1):
    # N: 정수의 개수
    N = int(input())
    
    result = []
    numbers = list(map(int, input().split()))
    
    for _ in range(0, N, 2):
        max_num = numbers.pop(numbers.index(max(numbers)))
        min_num = numbers.pop(numbers.index(min(numbers)))
        
        result.append(max_num)
        result.append(min_num)
    
    
    print(f'#{test_case}', *result[:10])