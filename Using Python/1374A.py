def main():
    t = int(input())
    for _ in range(t):
        x, y, n = map(int, input().split())
        ans = n - (n % x) + y
        if ans <= n:
            print(ans)
        else:
            print(n - (n % x) - (x - y))

if __name__ == "__main__":
    main()
