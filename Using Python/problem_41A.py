def is_translation(s, t):
    return s == t[::-1]

# Input reading
s = input()
t = input()


if is_translation(s, t):
    print("YES")
else:
    print("NO")
