def solution(a, b, n):
    answer = 0
    
    while n >= a:
        remain = n % a
        new_cola  = (n // a) * b
        answer += new_cola
        n = new_cola + remain
        
    return answer