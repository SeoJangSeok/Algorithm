def solution(s, skip, index):
    answer = ''
    skipped = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
    for i in s:
        answer += skipped[(skipped.index(i) + index) % len(skipped)]
        
    return answer