from collections import Counter

def solution(k, tangerine):
    # 크기별 개수 집계
    counts = Counter(tangerine)
    
    sorted_counts = sorted(counts.values(), reverse=True)
    
    answer = 0
    
    for count in sorted_counts:
        k -= count
        answer += 1
        if k <= 0:
            break
            
    return answer