# 백트래킹 사용
def dfs(row, col):
    if maze[row][col] == 3: # 도착점에 도달하면
        return 1
    
    # 현재 위치 방문 처리
    visited[row][col] = 1
    
    for dr, dc in moves:
        next_row, next_col = row + dr, col + dc
        
        if 0 <= next_row < N and 0 <= next_col < N: # 미로 범위 내에 있는지 확인
            if maze[next_row][next_col] != 1 and visited[next_row][next_col] == 0: # 벽이 아니고 방문하지 않은 곳이면
                if dfs(next_row, next_col): # 다음 위치로 이동
                    return 1
    
    # 현재 위치에서 도착점을 찾지 못하면 방문 처리 취소
    visited[row][col] = 0
    
    return 0

T = int(input())

for test_case in range(1, T + 1):
    # N: 미로의 크기
    N = int(input())
    
    maze = []
    visited = [[0] * N for _ in range(N)]
    
    start = (None, None) # 출발점 좌표
    
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상하좌우 이동 좌표
    
    for i in range(N):
        # 미로의 통로와 벽에 대한 정보
        # 0: 통로, 1: 벽, 2: 출발점, 3: 도착점
        row = list(map(int,input()))
        maze.append(row)
        if 2 in row:
            start = (i, row.index(2)) # 출발점 좌표 저장

    print(f'#{test_case} {dfs(start[0], start[1])}')