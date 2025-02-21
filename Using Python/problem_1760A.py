def solve():
    t = int(input().strip())  
    for _ in range(t):
        a, b, c = map(int, input().split())  
        if (a > b and a < c) or (a > c and a < b):
            print(a)
        elif (b > a and b < c) or (b > c and b < a):
            print(b)
        else:
            print(c)

solve()
