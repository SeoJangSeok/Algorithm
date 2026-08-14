def solution(s):
    answer = ''
    new_word = True

    for ch in s:
        if ch == ' ':
            answer += ch
            new_word = True
        else:
            if new_word:
                answer += ch.upper()
                new_word = False
            else:
                answer += ch.lower()

    return answer