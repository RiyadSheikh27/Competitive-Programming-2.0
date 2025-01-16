def solve():
    n, k = map(int, input().split())

    for i in range(n):
        for ch in range(k):
            print(chr(ord('a') + ch), end="")
    print()

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
