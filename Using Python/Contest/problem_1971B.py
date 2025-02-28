import sys
import math

def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x

def find_perfect_permutation(n):
    if n == 1:
        return -1
    
    permutation = list(range(n, 0, -1))
    prefix_sum = 0
    for num in permutation:
        prefix_sum += num
        if is_perfect_square(prefix_sum):
            return -1
    
    return permutation

def riyad():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        permutation = find_perfect_permutation(n)
        if permutation == -1:
            results.append("-1")
        else:
            results.append(" ".join(map(str, permutation)))
    
    print("\n".join(results))

riyad()