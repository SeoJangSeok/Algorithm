def solution(message, spoiler_ranges):
    # 각 문자가 몇 번째 스포 방지 구간에 속하는지 기록
    spoiler_index = [-1] * len(message)

    for range_index, (start, end) in enumerate(spoiler_ranges):
        for i in range(start, end + 1):
            spoiler_index[i] = range_index

    normal_words = set()      # 스포 방지가 전혀 적용되지 않은 평문 단어
    spoiler_words = []        # (공개 시점, 단어 위치, 단어)

    start = 0

    # message 뒤에 공백이 하나 있다고 가정하여 마지막 단어까지 처리
    for end in range(len(message) + 1):
        if end == len(message) or message[end] == ' ':
            word = message[start:end]

            # 이 단어에 포함된 스포 방지 구간 번호
            ranges = spoiler_index[start:end]

            if all(index == -1 for index in ranges):
                normal_words.add(word)
            else:
                # 단어의 모든 스포 구간이 해제되는 시점
                reveal_time = max(ranges)
                spoiler_words.append((reveal_time, start, word))

            start = end + 1

    # 공개되는 순서:
    # 1. 스포 방지 구간 순서
    # 2. 동시에 공개되면 왼쪽 단어부터
    spoiler_words.sort()

    answer = 0
    revealed_words = set()

    for _, _, word in spoiler_words:
        if word not in normal_words and word not in revealed_words:
            answer += 1

        # 중요한 단어가 아니더라도 '이전에 공개된 단어'에는 포함
        revealed_words.add(word)

    return answer