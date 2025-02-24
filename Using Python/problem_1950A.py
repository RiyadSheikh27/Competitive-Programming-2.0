def solution(a, b, c):
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")

n = int(input())
for _ in range(n):
    a, b, c = map(int,input().split())
    solution(a, b, c)