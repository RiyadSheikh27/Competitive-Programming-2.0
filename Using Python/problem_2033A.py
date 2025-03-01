import sys

def riyad():
    t = int(sys.stdin.readline().strip())  
    results = []
    
    for _ in range(t):
        n = int(sys.stdin.readline().strip())  
        n = abs(n)  
        results.append("Kosuke" if n % 2 else "Sakurako")  
    
    sys.stdout.write("\n".join(results) + "\n")  

riyad()
