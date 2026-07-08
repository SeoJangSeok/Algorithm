def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        limit_hour = schedules[i] // 100
        limit_min = schedules[i] % 100 + 10
        
        if limit_min >= 60:
            limit_hour += 1
            limit_min -= 60
        
        limit_time = limit_hour * 100 + limit_min
        
        for j in range(7):
            day = (startday + j - 1) % 7 + 1
            
            if day == 6 or day == 7:
                continue
            
            arrive_time = timelogs[i][j]
            
            if arrive_time > limit_time:
                break
        else:
            answer += 1
    return answer