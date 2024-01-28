word = input().strip()

uppercase_count = sum(1 for char in word if char.isupper())
lowercase_count = sum(1 for char in word if char.islower())

if uppercase_count > lowercase_count:
    print(word.upper())
else:
    print(word.lower())
