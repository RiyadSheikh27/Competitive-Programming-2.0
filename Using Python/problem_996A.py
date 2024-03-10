def main():
    a = [100, 20, 10, 5, 1]
    n = int(input())
    ans = 0

    for i in range(5):
        ans += n // a[i]
        n %= a[i]

    print(ans)


if __name__ == "__main__":
    main()
