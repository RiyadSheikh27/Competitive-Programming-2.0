package Codeforces_Problems;

import java.util.Scanner;

public class problem1328A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();
        while (t-- > 0) {
            long a = scanner.nextLong();
            long b = scanner.nextLong();

            if (a % b == 0) {
                System.out.println(0);
                continue;
            }

            long div = a / b;
            long pls = (div + 1) * b;
            System.out.println(pls - a);
        }

        scanner.close();
    }
}
