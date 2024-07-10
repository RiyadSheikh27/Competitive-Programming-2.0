import sys


def main():
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    results = []

    for _ in range(t):
        n = int(data[index])
        a = int(data[index + 1])
        b = int(data[index + 2])
        index += 3

        c = "abcdefghijklmnopqrstuvwxyz"
        s = c[:b]

        result = ""
        k = 0
        for _ in range(n):
            result += s[k]
            k += 1
            if k == b:
                k = 0

        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
