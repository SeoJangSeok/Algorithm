def solution(keymap, targets):
    answer = []
    d = dict()
    
    for keys in keymap:
        for key in keys:
            if key in d:
                d[key] = min(keys.index(key) + 1, d[key])
            else:
                d[key] = keys.index(key) + 1
    
    for target in targets:
        count = 0
        for i in target:
            if i not in d:
                answer.append(-1)
                break
            
            count += d[i]
        else:
            answer.append(count)
        
    return answer