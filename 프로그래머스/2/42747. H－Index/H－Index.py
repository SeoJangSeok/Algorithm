def solution(citations):
    citations.sort(reverse=True) # 내림차순(인용 횟수) 정렬
    
    for i, h in enumerate(citations):
        if i+1 > h: # 인용된 논문의 수 > 논문이 인용된 횟수
            return i
    return len(citations)