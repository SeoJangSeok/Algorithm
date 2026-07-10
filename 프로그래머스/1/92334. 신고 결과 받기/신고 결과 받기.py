def solution(id_list, report, k):
    answer = []
    # 사용자별 신고당한 횟수
    report_count = {id: 0 for id in id_list}
    
    # 사용자별 신고한 사람 목록
    report_logs = {id: [] for id in id_list}
    
    # 중복된 신고 제거
    report = set(report)
    
    for history in report:
        reporter, reported_user = history.split(' ')
        
        report_count[reported_user] += 1
        report_logs[reporter].append(reported_user)
        
    for id in id_list:
        mail_count = 0
        
        for reported_id in report_logs[id]:
            if report_count[reported_id] >= k:
                mail_count += 1
        answer.append(mail_count)
    
    return answer