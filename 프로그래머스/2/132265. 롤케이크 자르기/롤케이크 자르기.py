from collections import Counter

def solution(topping):
    answer = 0
    
    # 모든 토핑이 오른쪽에 있다고 가정
    right_cake = Counter(topping)
    # 왼쪽은 비어있는 상태
    left_cake = set()
    
    # 토핑을 하나씩 왼쪽으로 이동
    for t in topping:
        # 왼쪽 조각에 토핑 추가
        left_cake.add(t)
        
        # 오른쪽 조각에서 해당 토핑 개수 감소
        right_cake[t] -= 1
        # 개수가 0이 된 토핑은 dict에서 제거하여 종류 수(len)에 포함되지 않게 함
        if right_cake[t] == 0:
            del right_cake[t]
            
        # 왼쪽과 오른쪽의 토핑 종류(가짓수)가 같으면 정답 카운트 +1
        if len(left_cake) == len(right_cake):
            answer += 1
            
    return answer