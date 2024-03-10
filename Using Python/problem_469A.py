xy_levels = set()

n = int(input())

x = input().split()[1:]
y = input().split()[1:]

def push(levels):
    for level in levels:
        xy_levels.add(int(level))

push(x)
push(y)

print("I become the guy." if n == len(xy_levels) else "Oh, my keyboard!")
