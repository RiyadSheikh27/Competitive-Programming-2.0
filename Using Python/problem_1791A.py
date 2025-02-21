def solution():
    c = "codeforces"
    a = int(input())
    for _ in range(a):
        l = input().strip()
        if l in c:
            print("YES")
        else:
            print("No")

solution()