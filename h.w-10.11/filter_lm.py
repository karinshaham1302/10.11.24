import random
import statistics

# 1
random_list: list[int] = [random.randint(1, 100) for _ in range(50)]
print(random_list)

# a
print(list(filter(lambda x: x > 50, random_list)))

# b
print(list(filter(lambda x: x % 7 == 0, random_list)))

# c
print(list(filter(lambda x: 10 <= x <= 99, random_list)))

# d
print(list(filter(lambda x: 10 <= x <= 99 and (x // 10) == (x % 10), random_list)))

# e
print(list(filter(lambda x: 10 <= x <= 99 and (x // 10 + x % 10) == 9, random_list)))

# f
avg: float = statistics.mean(random_list)
print(list(filter(lambda x: x > avg, random_list)))

# g
max_num: int = max(random_list)
half_max: int = max_num / 2
print(list(filter(lambda x: x > half_max, random_list)))



# 2
games: list[str] = ['Fortnite', 'Grand Theft Auto V', 'The Elder Scrolls V: Skyrim', 'Dark Souls']
print(games)

# a
print(list(filter(lambda word: len(word) > 8, games)))

# b
print(list(filter(lambda word: word.upper().startswith('F'), games)))

# c
# לא הצלחתי לפתור..
print(list(filter(lambda word: word * 2, games)))

# d
print(list(filter(lambda word: 'V' in word, games)))
