def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        box = score[i : i+m]
        
        if len(box) < m:
            break
        
        answer += box[-1] * m
        
    return answer