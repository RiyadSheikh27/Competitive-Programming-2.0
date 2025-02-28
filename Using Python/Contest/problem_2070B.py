#Not Solved
def riyad(n, x, k, s):
    position = x
    zero_count = 0
    visited_positions = {x: 0}
    cycle_count = 0
    steps = 0
    
    while steps < k:
        for move in s:
            if move == 'L':
                position -= 1
            else:
                position += 1
            
            steps += 1
            if position == 0:
                zero_count += 1
                if steps >= k:
                    return zero_count
                cycle_count = 0
                visited_positions.clear()
                visited_positions[0] = steps
            
            elif position in visited_positions:
                cycle_length = steps - visited_positions[position]
                remaining_time = k - steps
                if cycle_length > 0:
                    full_cycles = remaining_time // cycle_length
                    zero_count += full_cycles * zero_count
                    steps += full_cycles * cycle_length
                
            visited_positions[position] = steps
            if steps >= k:
                return zero_count
    
    return zero_count

def process_input():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n, x, k = map(int, input().split())
        s = input().strip()
        results.append(str(riyad(n, x, k, s)))
    print("\n".join(results))

process_input()
