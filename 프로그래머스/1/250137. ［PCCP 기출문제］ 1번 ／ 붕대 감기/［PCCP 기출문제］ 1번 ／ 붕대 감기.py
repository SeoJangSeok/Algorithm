def solution(bandage, health, attacks):
    max_health = health
    t, x, y = bandage
    last_attack_time = attacks[-1][0]
    healing_time = 0
    attack_turn = 0
    
    for i in range(1, last_attack_time + 1):
        if i == attacks[attack_turn][0]:
            health -= attacks[attack_turn][1]
            healing_time = 0
            attack_turn += 1
            
            if health <= 0:
                return -1
        else:
            health = min(max_health, health + x)
            healing_time += 1
            
            if healing_time == t:
                health = min(max_health, health + y)
                healing_time = 0
    return health
    