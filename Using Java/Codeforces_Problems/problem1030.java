package Codeforces_Problems;
import java.util.Scanner;

public class problem1030 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int sum = 0;

        for (int i = 0; i < n; i++) {
            int x = input.nextInt();
            sum += x;
        }

        if (sum != 0) {
            System.out.println("HARD");
        } else {
            System.out.println("EASY");
        }

        // Close the scanner
        input.close();
    }
}
