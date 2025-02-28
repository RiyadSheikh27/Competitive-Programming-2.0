import sys
import heapq

def min_penalty(test_cases):
    results = []
    for case in test_cases:
        n, k, s, a = case
        required_blue = [i for i, char in enumerate(s) if char == 'B']
        
        if not required_blue:
            results.append(0)
            continue
        
        segments = []
        start = required_blue[0]
        for i in range(1, len(required_blue)):
            if required_blue[i] != required_blue[i-1] + 1:
                segments.append((start, required_blue[i-1]))
                start = required_blue[i]
        segments.append((start, required_blue[-1]))
        
        if len(segments) <= k:
            results.append(0)
            continue
        
        segment_penalties = []
        for seg in segments:
            start_idx, end_idx = seg
            max_penalty = max(a[start_idx:end_idx+1])
            segment_penalties.append((-max_penalty, start_idx, end_idx))
        
        heapq.heapify(segment_penalties)
        selected_segments = []
        for _ in range(k):
            max_p, start_idx, end_idx = heapq.heappop(segment_penalties)
            selected_segments.append((start_idx, end_idx))
        
        remaining_penalties = []
        for seg in segments:
            if seg not in selected_segments:
                start_idx, end_idx = seg
                for i in range(start_idx, end_idx + 1):
                    if s[i] == 'B':
                        remaining_penalties.append(a[i])
        
        if not remaining_penalties:
            results.append(0)
        else:
            results.append(max(remaining_penalties))
    
    return results

def riyad():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    test_cases = []
    for _ in range(t):
        n = int(input[ptr])
        k = int(input[ptr+1])
        ptr += 2
        s = input[ptr]
        ptr += 1
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        test_cases.append((n, k, s, a))
    results = min_penalty(test_cases)
    for res in results:
        print(res)

riyad()
