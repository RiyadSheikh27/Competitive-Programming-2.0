cards = int(input())
nums = [int(x) for x in input().split()]

s, d = 0, 0

for i in range(cards):
    if i % 2 == 0:  # Player S's turn
        s += max(nums[0], nums[-1])
    else:  # Player D's turn
        d += max(nums[0], nums[-1])
    if nums[0] > nums[-1]:
        nums.pop(0)
    else:
        nums.pop(-1)

print(f"{s} {d}")
