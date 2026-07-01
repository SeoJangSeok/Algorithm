def solution(numbers, hand):
    answer = ''
    
    key_pad = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2),
    '*':(3,0), 0:(3,1), '#':(3,2)
    }
    left = [1, 4, 7]
    right = [3, 6, 9]
    
    left_hand = '*'
    right_hand = '#'
    
    for i in numbers:
        if i in left:
            answer += 'L'
            left_hand = i
        elif i in right:
            answer += 'R'
            right_hand = i
        else: # 중간
            target_num = key_pad[i]
            left_pos = key_pad[left_hand]
            right_pos = key_pad[right_hand]
            
            left_dist = abs(target_num[0] - left_pos[0]) + abs(target_num[1] - left_pos[1])
            right_dist = abs(target_num[0] - right_pos[0]) + abs(target_num[1] - right_pos[1])
            
            if left_dist < right_dist:
                answer += 'L'
                left_hand = i
            elif right_dist < left_dist:
                answer += 'R'
                right_hand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = i
                else:
                    answer += 'R'
                    right_hand = i
    return answer