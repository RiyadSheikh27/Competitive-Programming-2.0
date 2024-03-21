MAX = 100000
MIN = -100000

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
b.sort()

res = 0

for i in range(n):
    for j in range(m):
        if abs(a[i] - b[j]) <= 1:
            res += 1
            a[i] = MIN
            b[j] = MAX

print(res)
