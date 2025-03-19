import sys


def main():
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n, k = int(data[index]), int(data[index + 1])
        index += 2

        a = [0] * n
        x = 1

        for i in range(k - 1, n, k):
            a[i] = x
            x += 1

        for i in range(n - 1, -1, -1):
            if a[i] == 0:
                a[i] = x
                x += 1

        results.append(" ".join(map(str, a)))

    sys.stdout.write("\n".join(results) + "\n")


main()
