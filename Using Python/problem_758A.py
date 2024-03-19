while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()

        max_val = arr[-1]
        total_sum = sum(abs(max_val - x) for x in arr[:-1])

        print(total_sum)
    except EOFError:
        break
