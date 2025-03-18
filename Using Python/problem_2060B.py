import sys


def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2

        a = list(map(int, data[index : index + n * m]))
        index += n * m

        pos_map = {a[i]: (i // m) + 1 for i in range(n * m)}
        sorted_a = sorted(a)

        ans = [pos_map[val] for val in sorted_a]

        valid = all(ans[i] == ans[i % n] for i in range(n, n * m))

        if not valid:
            results.append("-1")
        else:
            results.append(" ".join(map(str, ans[:n])))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
