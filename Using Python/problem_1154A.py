a = list(map(int, input().split()))
a.sort()

for i in range(3):
    print(a[3] - a[i], end=" ")

print()
