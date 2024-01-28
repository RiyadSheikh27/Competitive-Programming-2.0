n, h = map(int, input().split())
a = list(map(int, input().split()))
t = 0

for i in a:
    if i > h:
        t += 2
    else:
        t += 1

print(t)
