T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    n = N // 10
    
    dp = [0] * (n + 1)
    
    dp[1] = 1
    
    if n >= 2:
        dp[2] = 3
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
    
    print(f'#{test_case} {dp[n]}')