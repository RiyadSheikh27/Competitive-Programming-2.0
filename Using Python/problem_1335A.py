import math

def main():
    t = int(input())
    
    while t > 0:
        ans = 0
        n = float(input())
        ans = math.ceil((n / 2) - 1)
        print(ans)
        t -= 1

if __name__ == "__main__":
    main()
***Comment***