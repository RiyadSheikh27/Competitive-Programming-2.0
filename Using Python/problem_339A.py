def helpful_maths(expression):

    digits = [int(char) for char in expression if char.isdigit()]

    digits.sort()

    sorted_expression = '+'.join(map(str, digits))

    return sorted_expression

expression = input().strip()

result = helpful_maths(expression)
print(result)
