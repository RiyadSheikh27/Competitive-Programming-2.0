def main():
    n = int(input())
    number = 0
    h, a = [], []

    for _ in range(n):
        hi, ai = map(int, input().split())
        h.append(hi)
        a.append(ai)

        for j in range(len(h) - 1):
            if h[-1] == a[j]:
                number += 1
            if a[-1] == h[j]:
                number += 1

    print(number)


if __name__ == "__main__":
    main()
