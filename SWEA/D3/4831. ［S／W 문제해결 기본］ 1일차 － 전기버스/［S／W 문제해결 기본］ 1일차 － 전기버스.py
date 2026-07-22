T = int(input())

for test_case in range(1, T + 1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점 정류장
    # M : 충전기가 설치된 정류장 개수
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장 위치
    charge_station = list(map(int, input().split()))
    # 충전 횟수, 현재 위치 초기화
    count = current = 0

    while current + K < N:
        for step in range(K, 0, -1):
            # 현재 위치 + 이동 거리만큼 이동했을 때 충전기가 있는 정류장일 경우
            if (current + step) in charge_station:
                current += step
                count += 1
                break
        else:
            count = 0
            break
    print('#{} {}'.format(test_case, count))