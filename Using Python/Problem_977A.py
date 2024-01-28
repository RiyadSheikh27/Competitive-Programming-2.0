def wrong_subtraction(n, k):
    for _ in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1
    return n

# Example usage:
n, k = map(int, input().split())
result = wrong_subtraction(n, k)
print(result)
