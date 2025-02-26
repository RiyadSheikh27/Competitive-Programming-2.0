def solution(t):
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        max_product = 0

        for i in range(n):
            modified_a = a[:]
            modified_a[i] += 1  
            
            product = 1
            for num in modified_a:
                product *= num  
            
            max_product = max(max_product, product)  

        print(max_product)

t = int(input())
solution(t)
