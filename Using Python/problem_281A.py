def capitalize_word(word):
    result = word[0].upper() + word[1:]
    return result

word = input().strip()

result = capitalize_word(word)
print(result)
