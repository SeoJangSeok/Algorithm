def solution(number, limit, power):
    # 1 ~ number 까지 각 수의 약수 개수 구하기
    n_divisor = []
    answer = 0
    
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if j == i // j:
                    count += 1
                else:
                    count += 2
        n_divisor.append(count)
    # 각 수가 limit를 넘지 않는지 확인
    for n in n_divisor:
    # 넘으면 power로 대체
        if n > limit:
            answer += power
        else:
            answer += n
    return answer
    