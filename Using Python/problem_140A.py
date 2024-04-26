t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if b < a:
        a, b = b, a
    sub = b - a
    div = sub // 10
    mod = sub % 10
    sum_val = div
    if mod > 0:
        sum_val += 1
    print(sum_val)

//This is Riyad here.
