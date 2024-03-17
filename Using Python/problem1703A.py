class A:
    def yesno(self):
        t = int(input())
        for _ in range(t):
            s = input().lower()
            if s == "yes":
                print("YES")
            else:
                print("NO")


obj = A()
obj.yesno()
