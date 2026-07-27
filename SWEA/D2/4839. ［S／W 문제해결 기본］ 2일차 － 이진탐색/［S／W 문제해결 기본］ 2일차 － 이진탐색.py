def binary_search(last_page, target):
    # l: 탐색할 범위 중 가장 왼쪽 페이지
    # r: 탐색할 범위 중 가장 오른쪽 페이지
    l, r = 1, last_page
    count = 0
    
    while l <= r:
        c = (l + r) // 2
        count += 1
        
        if c == target:
            return count
        elif c < target:
            l = c
        else:
            r = c

T = int(input())

for test_case in range(1, T+1):
    # r: 책의 마지막 페이지
    # Pa: A가 찾을 페이지
    # Pb: B가 찾을 페이지
    r, Pa, Pb = map(int, input().split())
    
    count_A = binary_search(r, Pa)
    count_B = binary_search(r, Pb)
    
    if count_A < count_B:
        result = 'A'
    elif count_A > count_B:
        result = 'B'
    else:
        result = 0
    
    print(f'#{test_case} {result}')