def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for c in new_id:
        if c.isalnum() or c in '-_.':
            answer += c
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    answer = answer.strip('.')
    # 5단계
    answer = 'a' if answer == '' else answer
    # 6단계
    answer = answer[:15].rstrip('.')
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer
