import random

# 3
random_list: list[int] = [random.randint(-50, 50) for _ in range(20)]
print(random_list)

# a
print(list(map(lambda x: x ** 3, random_list)))

# b
print(list(map(lambda x: x % 10, random_list)))

# c
print(list(map(lambda x: (9 / 5) + 32, random_list)))

# d
print(list(map(lambda x: 'positive' if x > 0 else 'negative', random_list)))



# 4
fruits: list[str] = ['Apple', 'Banana', 'Orange', 'Mango', 'Strawberry', 'Pineapple', 'Grapes', 'Watermelon']
print(fruits)

# a
print(list(map(lambda word: word[::-1], fruits)))

# b
print(list(map(lambda word: word[0], fruits)))

# c
print(list(map(lambda word: word.upper(), fruits)))

# d
print(list(map(lambda word: word[len(word) // 2], fruits)))

# e
print(list(map(lambda word: word + '!' if word.endswith('s') else ' - ', fruits)))
