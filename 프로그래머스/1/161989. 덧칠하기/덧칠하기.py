def solution(n, m, section):
    answer = 0
    painted_loc = 0
    
    for s in section:
        if s > painted_loc:
            painted_loc = s + m - 1
            answer += 1
            
    return answer