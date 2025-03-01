def max_valid_sequences(a):
    mx = 0
    for i in range(-100, 101):
        a[2] = i
        cnt = 0
        if a[2] == a[1] + a[0]:
            cnt += 1
        if a[3] == a[2] + a[1]:
            cnt += 1
        if a[4] == a[3] + a[2]:
            cnt += 1
        mx = max(mx, cnt)
    return mx

t = int(input().strip())

for _ in range(t):
    a = [0] * 5
    a[0], a[1], a[3], a[4] = map(int, input().split())
    print(max_valid_sequences(a))
