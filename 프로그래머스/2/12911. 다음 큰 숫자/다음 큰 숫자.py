def solution(n):
    count = bin(n).count('1')
    
    n += 1
    
    while bin(n).count('1') != count:
        n += 1
        
    return n