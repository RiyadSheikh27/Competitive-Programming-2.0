def main():
    while True:
        try:
            n = int(input())
            sum = 0

            for _ in range(n):
                shape = input().strip()

                if shape == "Tetrahedron":
                    sum += 4
                elif shape == "Cube":
                    sum += 6
                elif shape == "Octahedron":
                    sum += 8
                elif shape == "Dodecahedron":
                    sum += 12
                elif shape == "Icosahedron":
                    sum += 20

            print(sum)

        except EOFError:
            break

if __name__ == "__main__":
    main()
