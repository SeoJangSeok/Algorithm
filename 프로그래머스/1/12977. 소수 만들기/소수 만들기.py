def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                total = nums[i] + nums[j] + nums[k]
                
                for n in range(2, int(total**0.5)+1):
                    if total % n == 0:
                        break
                else:
                    answer += 1
    return answer