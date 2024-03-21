from collections import defaultdict

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

def longest_common_subsequence(dp, s1, s2):
    for i in range(len(s2) + 1):
        for j in range(len(s1) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(s2)][len(s1)]

def divide_and_conquer(a, k, l, r):
    pivot = a[r]
    res = l
    k = len(a) - k
    for i in range(l, r):
        if a[i] <= pivot:
            a[res], a[i] = a[i], a[res]
            res += 1
    a[res], a[r] = a[r], a[res]
    if res > k:
        return divide_and_conquer(a, k, l, res - 1)
    elif res < k:
        return divide_and_conquer(a, k, res + 1, r)
    else:
        return a[res]

def solve_problem():
    n = int(input())
    a = list(map(int, input().split()))
    b = defaultdict(int)
    for num in a:
        b[num % 10] += 1
    
    res = False
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if (i + j + k) % 10 == 3:
                    c = b.copy()
                    c[i] -= 1
                    c[j] -= 1
                    c[k] -= 1
                    flag = all(val >= 0 for val in c.values())
                    if flag:
                        res = True
                        print("YES")
                        return
    if not res:
        print("NO")

if __name__ == "__main__":
    tcs = int(input())
    for _ in range(tcs):
        solve_problem()
