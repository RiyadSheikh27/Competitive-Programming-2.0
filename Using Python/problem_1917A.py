t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    zero = any(x == 0 for x in v)
    pos = sum(1 for x in v if x > 0)
    if zero:
        print(0)
        continue
    if pos == n:
        print(1)
        print(1, 0)
        continue
    neg = n - pos
    if neg % 2 == 1:
        print(0)
    else:
        print(1)
        print(1, 0)
