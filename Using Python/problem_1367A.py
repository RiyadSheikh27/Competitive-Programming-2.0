def solve():
    s = input()
    ssize = len(s)
    ans = s[0]
    for i in range(1, ssize - 1, 2):
        ans += s[i]
    ans += s[ssize - 1]
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
