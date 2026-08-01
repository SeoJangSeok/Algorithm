T = int(input())

for test_case in range(1, T + 1):
        str1 = set(input())
        str2 = input()
        
        char_counts = {char: 0 for char in str1}
        
        for char in str2:
            if char in char_counts:
                char_counts[char] += 1
            
        print(f'#{test_case} {max(char_counts.values())}')