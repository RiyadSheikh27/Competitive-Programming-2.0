package Codeforces_Problems;

import java.util.Scanner;

import java.util.Scanner;

public class problem705A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        if (n == 1) {
            System.out.println("I hate it");
        } else if (n > 1) {
            System.out.print("I hate that");
            for (int i = 2; i < n; i++) {
                if (i % 2 == 1 && i != n) {
                    System.out.print(" I hate that");
                } else if (i % 2 == 0 && i != n) {
                    System.out.print(" I love that");
                }
            }

            if (n % 2 == 0 && n > 1) {
                System.out.println(" I love it");
            } else if (n > 1) {
                System.out.println(" I hate it");
            }
        }

        scanner.close();
    }
}
