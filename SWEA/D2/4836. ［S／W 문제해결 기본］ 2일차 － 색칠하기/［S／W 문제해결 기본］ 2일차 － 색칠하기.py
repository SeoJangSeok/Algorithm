T = int(input())

for test_case in range(1, T+1):
    grid = [[0] * 10 for _ in range(10)] # 10x10 격자판 생성
    N = int(input()) # 칠할 영역의 개수
    
    for _ in range(N):
        # r1, c1: 왼쪽 위 모서리 인덱스
        # r2, c2: 오른쪽 아래 모서리 인덱스
        # color = 1 (빨강), color = 2 (파랑)
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 영역 칠하기
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                if grid[row][col] == 0: # 아직 칠해지지 않은 경우
                    grid[row][col] = color
                elif grid[row][col] != color: # 다른 색으로 칠해진 경우
                    grid[row][col] = 3 # 보라색
        
    # 보라색이 된 칸 수 구하기
    purple_count = sum(row.count(3) for row in grid)
    
    print(f'#{test_case} {purple_count}')