import sys

for line in sys.stdin:
    n, k = map(int, line.split())

    res = 240 - k
    sum_time = 0
    solved_problems = 0

    for i in range(1, n + 1):
        sum_time += 5 * i

        if sum_time > res:
            break

        solved_problems += 1

    print(solved_problems)
