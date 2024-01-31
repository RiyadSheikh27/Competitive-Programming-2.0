package problem_136A;

import java.util.Scanner;
import java.util.Vector;

public class main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        Vector<Integer> f = new Vector<>(n + 1);

        for (int i = 1; i <= n; ++i) {
            int p = input.nextInt();
            f.add(p, i);
        }

        System.out.print(f.get(1));
        for (int i = 2; i <= n; ++i) {
            System.out.print(" " + f.get(i));
        }
        System.out.println();
        input.close();
    }
}
