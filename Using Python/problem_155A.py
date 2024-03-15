t = int(input())
arr = list(map(int, input().split()))
min_val = max_val = arr[0]
c = 0

for num in arr:
    if num < min_val:
        min_val = num
        c += 1
    if num > max_val:
        max_val = num
        c += 1

print(c)
