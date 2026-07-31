def find_palindrome(board, N, M):
    # 가로 방향 탐색
    for row in range(N):
        for start_col in range(N - M + 1):
            row_substr = board[row][start_col:start_col+M] # 길이가 M인 부분 문자열
            if row_substr == row_substr[::-1]:
                return row_substr
            
    # 세로 방향 탐색
    for col in range(N):
        for start_row in range(N - M + 1):
            col_substr = ''.join(board[start_row+i][col] for i in range(M)) # 길이가 M인 부분 문자열
            if col_substr == col_substr[::-1]:
                return col_substr


T = int(input())

for test_case in range(1, T+1):
    # N x N 크기의 글자판
    # 길이가 M인 회문
    N, M = map(int, input().split())
    
    # 길이가 N인 N개의 글자 입력
    board = [input() for _ in range(N)]
    
    palindrome = find_palindrome(board, N, M)
    
    print(f'#{test_case} {palindrome}')