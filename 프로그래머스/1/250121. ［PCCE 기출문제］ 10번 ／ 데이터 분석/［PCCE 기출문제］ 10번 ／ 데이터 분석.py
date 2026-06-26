def solution(data, ext, val_ext, sort_by):
    answer = []
    hash = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    for i in range(len(data)):
        if data[i][hash[ext]] < val_ext:
            answer.append(data[i])
    
    answer.sort(key=lambda x: x[hash[sort_by]])
    
    return answer