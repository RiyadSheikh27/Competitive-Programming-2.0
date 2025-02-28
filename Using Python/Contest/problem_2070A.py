#Solved by Md. Fazle Rabbi Riyad
def fizzbuzz(n):
    q = n // 15
    rem = n % 15
    return 3 * q + min(3, rem+ 1)

t = int(input()) 
for _ in range(t):
    n = int(input())
    print(fizzbuzz(n))