def main():
    length = int(input())
    string_input = input().lower()
    char_set = set(string_input)

    if len(char_set) == 26:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
