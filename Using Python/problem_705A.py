def solve():
    n = int(input())
    for i in range(n):
        if i & 1:
            print("I love", end=" ")
        else:
            print("I hate", end=" ")

        if i != n - 1:
            print("that", end=" ")
        else:
            print("it", end=" ")


def main():
    T = 1
    while T > 0:
        solve()
        T -= 1


if __name__ == "__main__":
    main()
