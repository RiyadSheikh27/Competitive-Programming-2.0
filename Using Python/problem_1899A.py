def solution(t):
    for _ in range(t):
        n = int(input())
        if n % 3 == 0:
            print("Second")
        else:
            print("First")

t = int(input())
solution(t)
