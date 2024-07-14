def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = []
        
        for i in range(n):
            temp = int(data[index + i])
            a.append(temp)
        
        index += n
        
        mx = -1e11
        sum_result = 0
        check = True
        
        for i in range(n):
            if check:
                if a[i] < 0:
                    if mx > -1e10:
                        sum_result += mx
                    mx = -1e11
                    check = False
            else:
                if a[i] > 0:
                    if mx > -1e10:
                        sum_result += mx
                    mx = -1e11
                    check = True
            
            mx = max(a[i], mx)
        
        if mx > -1e10:
            sum_result += mx
        
        results.append(sum_result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
