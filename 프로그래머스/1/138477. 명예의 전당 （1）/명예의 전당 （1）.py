def solution(k, score):
    answer = [] # 최하위 점수 저장
    HOF = [] # 명예의 전당
    
    # k 만큼 HOF에 점수 저장 and 점수 비교
    for i in score:
        if len(HOF) < k:
            HOF.append(i)
        else:
            HOF.sort(reverse=True)
            if HOF[-1] < i:
                HOF.pop()
                HOF.append(i)
        HOF.sort(reverse=True)
        answer.append(HOF[-1])
    return answer