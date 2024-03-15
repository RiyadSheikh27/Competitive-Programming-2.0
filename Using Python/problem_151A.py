n, k, l, c, d, p, nl, np = map(int, input().split())
result = min(min(k * l // nl, c * d), p // np) // n
print(result)
