def solution(lottos, win_nums):
    answer = []
    prize = [6, 6, 5, 4, 3, 2, 1]
    
    zero_count = 0
    correct_count = 0
    
    for i in lottos:
        if i == 0:
            zero_count += 1
        elif i in win_nums:
            correct_count += 1
    
    answer.append(prize[correct_count + zero_count])
    answer.append(prize[correct_count])
    
    return answer