m, n = map(int, input().split())
a = m * n
if m > n:
    b = a // m
else:
    b = a // n

if b % 2 == 0:
    print("Malvika")
else:
    print("Akshat")
