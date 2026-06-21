def solution(dartResult):
    scores = []
    num = ''
    
    for ch in dartResult:
        if ch.isdigit():
            num += ch
        
        elif ch in ['S', 'D', 'T']:
            score = int(num)
            if ch == 'D':
                score **= 2
            elif ch == 'T':
                score **= 3
            scores.append(score)
            num = ''
        
        elif ch == '*':
            scores[-1] *= 2
            if len(scores) >= 2:
                scores[-2] *= 2
        
        elif ch == '#':
            scores[-1] *= -1
    
    return sum(scores)