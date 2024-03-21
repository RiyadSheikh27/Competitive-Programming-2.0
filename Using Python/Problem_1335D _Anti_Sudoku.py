def solve_problem():
    a = [input() for _ in range(9)]
    for i in range(9):
        a[i] = a[i].replace('1', '2')
        print(a[i])

if __name__ == "__main__":
    tcs = int(input())
    for _ in range(tcs):
        solve_problem()
