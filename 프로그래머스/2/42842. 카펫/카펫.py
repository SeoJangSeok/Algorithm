def solution(brown, yellow):
    total = brown + yellow # 전체 카펫의 넓이
    
    for height in range(3, total+1):
        # height가 전체 넓이의 약수가 아니라면 직사각형 or 정사각형을 만들 수 없음
        if total % height != 0:
            continue
            
        width = total // height
        
        # 가로 길이 >= 세로 길이
        if width < height:
            continue
        
        if (width - 2) * (height - 2) == yellow:
            return [width, height]