arr = []
j = 0
for i in range(1, 1667):
    if i % 3 != 0 and i % 10 != 3:
        arr.append(i)
        j += 1

t = int(input())
while t > 0:
    k = int(input())
    print(arr[k - 1])
    t -= 1