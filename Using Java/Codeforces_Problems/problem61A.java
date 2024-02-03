package Codeforces_Problems;

import java.util.Scanner;

public class problem61A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String s1 = scanner.next();
        String s2 = scanner.next();

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) == s2.charAt(i)) {
                result.append('0');
            } else {
                result.append('1');
            }
        }
        System.out.println(result.toString());
    }
}
