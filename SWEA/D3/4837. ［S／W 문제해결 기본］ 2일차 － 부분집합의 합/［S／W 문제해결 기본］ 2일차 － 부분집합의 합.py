A = list(range(1, 13))

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    answer = 0

    for bit in range(1 << 12):
        cnt = 0
        total = 0

        for i in range(12):
            if bit & (1 << i):
                cnt += 1
                total += A[i]

        if cnt == N and total == K:
            answer += 1

    print(f'#{test_case} {answer}')