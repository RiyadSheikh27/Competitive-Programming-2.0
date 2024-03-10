n = int(input())

a = list(map(int, input().split()))

min_val = a[0]
min_index = 0
max_val = a[0]
max_index = 0

for i in range(n):
    if min_val >= a[i]:
        min_val = a[i]
        min_index = i
    if max_val < a[i]:
        max_val = a[i]
        max_index = i

if min_index < max_index:
    min_index = (n - 1) - min_index
    print(min_index + max_index - 1)
else:
    min_index = (n - 1) - min_index
    print(min_index + max_index)
