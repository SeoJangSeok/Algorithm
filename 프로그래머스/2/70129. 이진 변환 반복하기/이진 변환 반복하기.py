def solution(s):
    zero_count = 0
    turn = 0
    
    while s != '1':
        # s에 있는 0의 개수
        zero_count += s.count('0')
        # s의 모든 0을 제거
        s = s.replace('0', '')
        
        # s의 길이를 2진법으로 표현한 문자열로 변환
        s = f'{len(s):b}'
        
        turn += 1
    
    return [turn, zero_count]