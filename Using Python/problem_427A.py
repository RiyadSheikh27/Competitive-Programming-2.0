n = int(input())
arr = list(map(int, input().split()))

curr = 0
cnt = 0

for item in arr:
    curr += item
    if curr < 0:
        cnt += 1
        curr = 0

print(cnt)
