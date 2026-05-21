def solution(d, budget):
    answer = 0
    
    if sum(d) == budget:
        return len(d)
    
    d.sort()
    
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer
    