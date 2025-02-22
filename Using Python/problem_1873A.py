def solution():
    n = int(input()) 
    for _ in range(n):
        data = input().strip()  
        if data == "bca" or data == "cab":
            print("NO")
        else:
            print("YES")

solution()
