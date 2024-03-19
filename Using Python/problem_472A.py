mark = [False] * 1000001


def solv():
    for i in range(2, 1000001):
        if not mark[i]:
            for j in range(2 * i, 1000001, i):
                mark[j] = True


def main():
    solv()
    while True:
        try:
            x = int(input())
            for i in range(4, x - 3):
                if mark[i] and mark[x - i]:
                    print(i, x - i)
                    break
        except EOFError:
            break


if __name__ == "__main__":
    main()
