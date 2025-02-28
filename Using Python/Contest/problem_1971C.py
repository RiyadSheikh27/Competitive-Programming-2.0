import sys
from collections import deque

def riyad():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        st = int(data[idx + 1])
        en = int(data[idx + 2])
        idx += 3
        
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        if st == en:
            print(st)
            continue
        
        parent = [0] * (n + 1)
        visited = [False] * (n + 1)
        q = deque()
        q.append(st)
        visited[st] = True
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        
        path = []
        u = en
        while u != st:
            path.append(u)
            u = parent[u]
        path.append(st)
        path.reverse()
        
        if not path:
            print(-1)
            continue
        
        used = set(path)
        permutation = []
        for u in path[:-1]:
            permutation.append(u)
        for u in range(1, n + 1):
            if u not in used:
                permutation.append(u)
        permutation.append(path[-1])
        
        print(" ".join(map(str, permutation)))

riyad()