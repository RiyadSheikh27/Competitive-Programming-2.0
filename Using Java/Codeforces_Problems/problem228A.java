package Codeforces_Problems;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class problem228A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        List<Integer> s = new ArrayList<>();
        s.add(scanner.nextInt());
        s.add(scanner.nextInt());
        s.add(scanner.nextInt());
        s.add(scanner.nextInt());

        Collections.sort(s);
        s = removeDuplicates(s);

        System.out.println(4 - s.size());

        // Close the scanner to release resources
        scanner.close();
    }

    private static List<Integer> removeDuplicates(List<Integer> list) {
        List<Integer> result = new ArrayList<>();
        for (int i : list) {
            if (!result.contains(i)) {
                result.add(i);
            }
        }
        return result;
    }
}
