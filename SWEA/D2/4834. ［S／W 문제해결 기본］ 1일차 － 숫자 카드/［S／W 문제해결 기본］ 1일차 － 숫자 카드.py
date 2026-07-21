T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 카드 장수
    cards = list(map(int, input()))
    max_card = 0 # 가장 많은 카드에 적힌 숫자
    max_card_count = 0
    
    for card in set(cards):
        current_card_count = cards.count(card)
        
        if current_card_count > max_card_count:
            max_card_count = current_card_count
            max_card = card
        elif current_card_count == max_card_count:
            max_card = max(max_card, card)
        else:
            continue
    print(f'#{test_case} {max_card} {max_card_count}')