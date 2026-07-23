T = int(input())

for test_case in range(1, T+1):
    # N: 정수의 개수
    # M: 구간의 개수
    N, M = map(int, input().split())
    # N개의 정수 입력
    integers = list(map(int, input().split()))
    sum_list = []
    
    for i in range(0, len(integers)-M+1):
        sum_list.append(sum(integers[i:i+M]))
    
    print(f'#{test_case} {max(sum_list) - min(sum_list)}')