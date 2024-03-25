t = int(input())

for _ in range(t):
    r = int(input())
    if r <= 1399:
        res = 4
    elif r <= 1599:
        res = 3
    elif r <= 1899:
        res = 2
    else:
        res = 1
    print("Division", res)
