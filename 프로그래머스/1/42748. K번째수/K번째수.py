def solution(array, commands):
    answer = []
    
    for cmd in commands:
        i, j, k = cmd
        answer.append(sorted(array[i-1 : j])[k-1])
    
    return answer