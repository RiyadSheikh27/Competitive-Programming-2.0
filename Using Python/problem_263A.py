matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            moves = abs(i - 3) + abs(j - 3)

print(moves)
