def main():
    n, m = map(int, input().split())
    oddness = 0

    for i in range(n):
        if i % 2 == 0:
            print("#" * m)
        else:
            oddness += 1
            if oddness % 2 == 1:
                print("." * (m - 1) + "#")
            else:
                print("#" + "." * (m - 1))


if __name__ == "__main__":
    main()
