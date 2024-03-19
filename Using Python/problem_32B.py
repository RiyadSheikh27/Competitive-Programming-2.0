s = input()
s2 = ""
i = 0
while i < len(s):
    if s[i] == ".":
        s2 += "0"
    elif s[i] == "-" and s[i + 1] == ".":
        s2 += "1"
        i += 1
    elif s[i] == "-" and s[i + 1] == "-":
        s2 += "2"
        i += 1
    i += 1

print(s2)
