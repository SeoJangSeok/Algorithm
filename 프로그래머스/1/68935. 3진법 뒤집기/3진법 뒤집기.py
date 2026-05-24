def solution(n):
    ternery_reverse = ''
    r = 0
    
    while n > 0:
        r = n % 3
        n //= 3
        ternery_reverse += str(r)
        
    return int(ternery_reverse, 3)