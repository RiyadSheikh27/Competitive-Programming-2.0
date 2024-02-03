package Codeforces_Problems;

import java.util.Scanner;

public class problem486A {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        long n = input.nextLong();
        
        long result = (n % 2 == 0) ? n / 2 : (n + 1) / -2;

        System.out.println(result);
    }
}
