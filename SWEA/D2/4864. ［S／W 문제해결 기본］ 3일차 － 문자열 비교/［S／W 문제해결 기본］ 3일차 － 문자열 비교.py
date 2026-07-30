# KMP 알고리즘 사용
def make_lps(pattern):
    lps = [0] * len(pattern)
    # i: 현재 LPS 값을 구할 위치
    # j: 현재까지 일치한 접두사의 길이, i와 비교할 접두사의 인덱스
    i, j = 1, 0
    
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
        lps = make_lps(pattern)
        
        # i: text index
        # j: pattern index
        i, j = 0, 0
        
        while i < len(text):
        # 두 문자가 같은 경우
            if text[i] == pattern[j]:
                i += 1
                j += 1
                # Pattern의 마지막까지 일치한 경우
                if j == len(pattern):
                    return 1
            # 두 문자가 다른 경우
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return 0

T = int(input())

for test_case in range(1, T+1):
    pattern = input()
    text = input()
    
    result = kmp_search(text, pattern)
    
    print(f'#{test_case} {result}')