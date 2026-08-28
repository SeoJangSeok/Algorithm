def solution(n, words):
    # 이미 나온 단어를 저장할 집합 (첫 번째 단어 포함)
    seen = {words[0]}
    
    # 두 번째 단어부터 순회하며 조건 검사
    for i in range(1, len(words)):
        word = words[i]
        prev_word = words[i - 1]
        
        # 탈락 조건: 
        # 1. 이전 단어의 끝 글자와 현재 단어의 첫 글자가 안 맞음
        # 2. 이미 등장했던 단어임
        if word[0] != prev_word[-1] or word in seen:
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]
        
        # 탈락하지 않았으면 집합에 추가
        seen.add(word)
        
    # 탈락자가 없다면 [0, 0] 반환
    return [0, 0]