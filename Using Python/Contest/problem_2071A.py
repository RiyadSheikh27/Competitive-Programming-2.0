def can_spectator_be_same(k):
    return k % 3 == 1

def riyad():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        k = int(data[i])
        if can_spectator_be_same(k):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

riyad()