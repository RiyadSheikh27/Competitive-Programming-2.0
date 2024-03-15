import math

t = int(input())

for _ in range(t):
    n = int(input())

    digits = []
    j = 0

    while n > 0:
        if n % 10:
            ans = pow(10, j) * (n % 10)
            digits.append(ans)
        n //= 10
        j += 1

    length = len(digits)
    print(length)

    for digit in digits:
        print(digit, end=" ")

    print()
