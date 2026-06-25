def solution(X, Y):
    answer = []
    
    for num in '9876543210':
        count = min(X.count(num), Y.count(num))
        answer.append(num * count)
        
    answer = ''.join(answer)
    
    if answer == '':
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer