n = int(input())
s = input()

a = 0
b = 0

for char in s:
    if char == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print("Anton")
elif a < b:
    print("Danik")
else:
    print("Friendship")
