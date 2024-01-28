def lucky_number(num):
    count = 0
    for i in num:
        if i == '4' or i == '7':
            count += 1
    # print(count)
    if count == 4 or count == 7:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    num = input()
    print(lucky_number(num))
