import sys
from math import gcd
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()

        b = []
        cnt = 1
        i, j = 0, n - 1

        while i < j and cnt < 3:
            b.append(a[i])
            b.append(a[j])
            i += 1
            j -= 1
            cnt += 1

        if len(b) < 4:
            # Fill missing elements if needed (less than 4 due to small n)
            while len(b) < 4 and i <= j:
                b.append(a[i])
                i += 1

        ans = abs(b[0] - b[1]) + abs(b[1] - b[2]) + abs(b[2] - b[3]) + abs(b[3] - b[0])

        print(ans)


if __name__ == "__main__":
    main()
