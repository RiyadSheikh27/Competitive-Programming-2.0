def binary_search(arr, xx):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == xx:
            return mid
        if arr[mid] > xx:
            right = mid - 1
        if arr[mid] < xx:
            left = mid + 1
    return -1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def first_greater_element(arr, xx):
    length = len(arr) - 1
    start = 0
    ans = -1
    while start <= length:
        mid = (start + length) // 2
        if arr[mid] < xx:
            start = mid + 1
        else:
            ans = mid
            length = mid - 1
    return ans

def prefix_max(a):
    dp = [0] * len(a)
    dp[0] = 0
    for i in range(1, len(a)):
        dp[i] = max(dp[i - 1], a[i - 1])
    return dp

def solve_problem():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = [x - 1 for x in a]
    b = [x - 1 for x in b]

    p = [0] * n
    c = [0] * n

    for i in range(n):
        p[b[i]] = i

    for i in range(n):
        c[i] = p[a[i]]

    prefix = prefix_max(c)

    res = sum(1 for i in range(n) if c[i] < prefix[i])

    print(res)

if __name__ == "__main__":
    solve_problem()
