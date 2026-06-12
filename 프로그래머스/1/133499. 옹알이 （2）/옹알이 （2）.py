def solution(babbling):
    answer = 0
    
    baby = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        for able in baby:
            if able*2 not in word:
                word = word.replace(able, ' ')
                
        if word.isspace():
            answer += 1
    
    return answer