def solution(N, stages): # 전체 스테이지 개수, 사용자가 현재 멈춰있는 스테이지 번호
    # 해당 스테이지를 아직 클리어하지 못한 수 / 해당 스테이지에 도달한 플레이어 수
    answer = []
    
    total_player = len(stages)
    failure_rate = {}
    
    for i in range(1, N+1):
        if stages.count(i) == 0:
            failure_rate[i] = 0
            continue
        
        failure_rate[i] = stages.count(i) / total_player
        total_player -= stages.count(i)
        
    failure_rate = sorted(failure_rate.items(), key=lambda x: x[1], reverse=True)
    
    for i in failure_rate:
        answer.append(i[0])
    return answer