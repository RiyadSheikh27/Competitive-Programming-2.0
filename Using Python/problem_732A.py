k, r = map(int, input().split())
for i in range(1, 10):
    if (k * i) % 10 == r or (k * i) % 10 == 0:
        n = i
        break
print(n)