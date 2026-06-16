def solution(board, h, w):
    answer = 0
    
    dh = [0, 0, 1, -1]
    dw = [1, -1, 0, 0]
    
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        
        if 0 <= nh < len(board) and 0 <= nw < len(board):
            if board[nh][nw] == board[h][w]:
                answer += 1
                
    return answer