def solution(elements):
    n = len(elements)
    extended = elements * 2
    sums = set()
    
    # 부분 수열의 길이 length (1 ~ n) 
    for length in range(1, n + 1):
        # 시작 인덱스 i (0 ~ n-1)
        for i in range(n):
            # 길이 length 만큼의 연속 부분 수열의 합 계산
            sub_sum = sum(extended[i : i + length])
            sums.add(sub_sum)
    
    return len(sums)